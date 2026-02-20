# WSL + Windows Playwright MCP 配置指南

本文档记录了在 WSL 环境中配置 Playwright MCP，使其能够控制 Windows 浏览器的完整流程。

## 架构说明

```
┌─────────────────────────────────────────────────────────────┐
│  Windows 主机                                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Playwright MCP Server (HTTP Mode)                  │   │
│  │  监听: 127.0.0.1:8931                                │   │
│  │  端口转发: 0.0.0.0:8931 → 127.0.0.1:8931            │   │
│  └─────────────────────────────────────────────────────┘   │
│                          ↑                                  │
│  ┌─────────────────┐    │    ┌─────────────────────────┐   │
│  │ vEthernet (WSL) │────┼────│ Chromium 浏览器         │   │
│  │ 172.30.224.1    │    │    │ chromium-1200           │   │
│  └─────────────────┘    │    └─────────────────────────┘   │
└─────────────────────────┼───────────────────────────────────┘
                          │ 端口转发
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  WSL2 (Linux)                                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Trae / AI Agent                                    │   │
│  │  MCP 客户端配置: http://172.30.224.1:8931/mcp       │   │
│  └─────────────────────────────────────────────────────┘   │
│  eth0: 172.30.230.164                                       │
│  默认网关: 172.30.224.1 → Windows WSL 网卡                  │
└─────────────────────────────────────────────────────────────┘
```

## 版本对应关系

| 组件 | 版本 | 说明 |
|-----|------|------|
| Playwright MCP Server | 1.0.11 | `@executeautomation/playwright-mcp-server` |
| Playwright | 1.57.0 | 对应 `chromium-1200` |
| Chromium | build v1200 | `143.0.7499.4` |

> ⚠️ **重要**: MCP 服务器版本与 Playwright 浏览器版本必须匹配，否则会报 "Executable doesn't exist" 错误。

---

## 一、Windows 端配置

### 1. 安装 Playwright 浏览器驱动

```powershell
# 安装对应版本的 Chromium (chromium-1200)
npx -y playwright@1.57.0 install chromium
```

安装位置：`C:\Users\<用户名>\AppData\Local\ms-playwright\chromium-1200`

### 2. 启动 MCP 服务器

```powershell
# 启动 Playwright MCP Server (HTTP 模式)
npx -y @executeautomation/playwright-mcp-server --port 8931
```

成功启动后会显示：

```
==============================================
Playwright MCP Server (HTTP Mode)
==============================================
Listening: 127.0.0.1:8931 (localhost only)
Version: 1.0.11
...
```

### 3. 配置端口转发

由于 MCP 服务器只监听 `127.0.0.1`（localhost），需要配置端口转发让 WSL 能够访问：

```powershell
# 添加端口转发规则
netsh interface portproxy add v4tov4 listenport=8931 listenaddress=0.0.0.0 connectport=8931 connectaddress=127.0.0.1

# 验证规则
netsh interface portproxy show all
```

### 4. 配置防火墙规则

```powershell
# 添加防火墙入站规则
New-NetFirewallRule -DisplayName "Playwright MCP" -Direction Inbound -LocalPort 8931 -Protocol TCP -Action Allow

# 验证规则
Get-NetFirewallRule -DisplayName "Playwright MCP"
```

### 5. 启动 IP Helper 服务

IP Helper 服务负责端口转发功能：

```powershell
# 检查服务状态
Get-Service iphlpsvc

# 如果未运行，启动服务
net start iphlpsvc
```

### 6. 获取 WSL 网卡 IP

```powershell
# 查看 WSL 网卡 IP
ipconfig

# 找到 "vEthernet (WSL (Hyper-V firewall))" 对应的 IPv4 地址
# 示例: 172.30.224.1
```

---

## 二、WSL 端配置

### 1. 获取 Windows 主机 IP

在 WSL 中运行：

```bash
# 方法1：通过默认网关获取（推荐）
ip route | grep default | awk '{print $3}'

# 方法2：通过 resolv.conf 获取（可能不准确）
cat /etc/resolv.conf | grep nameserver | awk '{print $2}'
```

> ⚠️ **注意**: 如果使用了 VPN 或代理，`resolv.conf` 中的 DNS 可能是虚拟地址，建议使用方法1。

### 2. 测试连接

```bash
# 测试 MCP 服务器是否可访问
curl http://<Windows_IP>:8931/health

# 成功响应示例：
# {"status":"ok","version":"1.0.11","activeSessions":0}
```

### 3. 配置 MCP 客户端

编辑 MCP 配置文件：`~/.trae-cn-server/data/Machine/mcp.json`

```json
{
  "mcpServers": {
    "Playwright": {
      "url": "http://172.30.224.1:8931/mcp",
      "type": "http"
    }
  }
}
```

> 将 `172.30.224.1` 替换为你实际的 Windows WSL 网卡 IP。

### 4. 重启 Trae

配置完成后，重启 Trae 使配置生效。

---

## 三、日常使用

### 启动流程

每次使用前，需要在 Windows 上启动 MCP 服务器：

```powershell
# 1. 检查端口是否被占用
netstat -ano | findstr :8931

# 如果有进程占用，杀掉它
# taskkill /PID <进程ID> /F

# 2. 启动 MCP 服务器
npx -y @executeautomation/playwright-mcp-server --port 8931

# 3. 确保 IP Helper 服务运行
net start iphlpsvc
```

### 常用 Playwright MCP 工具

| 工具 | 功能 |
|-----|------|
| `playwright_navigate` | 导航到 URL |
| `playwright_screenshot` | 截图 |
| `playwright_get_visible_text` | 获取可见文本 |
| `playwright_get_visible_html` | 获取 HTML |
| `playwright_click` | 点击元素 |
| `playwright_fill` | 填写表单 |
| `playwright_evaluate` | 执行 JavaScript |
| `playwright_close` | 关闭浏览器 |

### 截图保存位置

截图保存在 Windows 的 Downloads 目录：

```
C:\Users\<用户名>\Downloads\
```

WSL 中可通过以下路径访问：

```
/mnt/c/Users/<用户名>/Downloads/
```

---

## 四、常见问题排查

### 问题1：连接被拒绝 (Connection refused)

**症状**：
```
curl: (7) Failed to connect to <IP> port 8931
```

**排查步骤**：

1. 检查 MCP 服务器是否运行：
   ```powershell
   netstat -ano | findstr :8931
   ```

2. 检查端口转发规则：
   ```powershell
   netsh interface portproxy show all
   ```

3. 检查 IP Helper 服务：
   ```powershell
   Get-Service iphlpsvc
   net start iphlpsvc
   ```

4. 检查防火墙规则：
   ```powershell
   Get-NetFirewallRule -DisplayName "Playwright MCP"
   ```

### 问题2：浏览器驱动不存在 (Executable doesn't exist)

**症状**：
```
Executable doesn't exist at C:\Users\...\chromium-1200\chrome.exe
```

**原因**：Playwright 版本与 MCP 服务器不匹配。

**解决方案**：
```powershell
# 安装正确版本
npx -y playwright@1.57.0 install chromium
```

### 问题3：MCP 服务器崩溃

**症状**：
```
Error: Not connected
spawn npx ENOENT
```

**解决方案**：
```powershell
# 杀掉残留进程
taskkill /PID <进程ID> /F

# 重新启动
npx -y @executeautomation/playwright-mcp-server --port 8931
```

### 问题4：IP 地址变化

WSL 或 Windows 重启后，IP 地址可能变化。

**解决方案**：
```bash
# 重新获取 Windows IP
ip route | grep default | awk '{print $3}'

# 更新 MCP 配置文件中的 IP 地址
```

---

## 五、参考链接

- [executeautomation/mcp-playwright](https://github.com/executeautomation/mcp-playwright) - Playwright MCP Server
- [Playwright 官方文档](https://playwright.dev/)
- [WSL 网络配置](https://learn.microsoft.com/zh-cn/windows/wsl/networking)

---

## 六、快速命令参考

### Windows PowerShell

```powershell
# 一键启动（完整流程）
net start iphlpsvc; npx -y @executeautomation/playwright-mcp-server --port 8931

# 检查状态
netstat -ano | findstr :8931
netsh interface portproxy show all
Get-Service iphlpsvc

# 清理端口
taskkill /PID <PID> /F
```

### WSL Bash

```bash
# 获取 Windows IP
ip route | grep default | awk '{print $3}'

# 测试连接
curl http://$(ip route | grep default | awk '{print $3}'):8931/health
```

---

*文档创建日期：2026-02-19*
