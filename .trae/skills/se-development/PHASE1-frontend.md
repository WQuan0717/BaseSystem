# PHASE 1: Frontend UI/UX + Mock Data

## ⚠️ IMPORTANT

**You are in PHASE 1. Do NOT work on backend. Do NOT read PHASE 2 files.**

---

## YOUR TASK NOW

Complete frontend UI/UX design with mock data.

---

## STEP 1: UI/UX Design

### 1.1 Query Design System

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<project type> <keywords>" --design-system
```

**Example for a dashboard app:**
```bash
python3 skills/ui-ux-pro-max/scripts/search.py "industrial design simulation dashboard" --design-system
```

### 1.2 Document Design System

Create `src/design-system.md`:

```markdown
# Design System

## Color Palette
- Primary: #XXXXXX
- Secondary: #XXXXXX
- Accent: #XXXXXX

## Typography
- Font Family: XXX
- Heading Size: Xpx
- Body Size: Xpx

## Components
- Button: ...
- Card: ...
- Input: ...
```

---

## STEP 2: Frontend Structure

### 2.1 Create Directory Structure

```
src/
├── views/           # Page components
├── components/       # Reusable components
├── mocks/           # Mock data
│   ├── data/        # Mock JSON data
│   ├── handlers/     # Mock API handlers
│   └── index.ts     # Mock server entry
├── stores/          # State management
├── styles/          # CSS/styling
└── design-system.md # Design tokens
```

### 2.2 Create Mock Data

**`src/mocks/data/users.json`**
```json
[]
```

**`src/mocks/handlers/auth.ts`**
```typescript
export const mockAuthHandlers = {
  login: (data: any) => {
    return {
      success: true,
      user: { id: 1, name: 'Test User', email: data.email }
    };
  },
  register: (data: any) => {
    return {
      success: true,
      user: { id: 1, name: data.username, email: data.email }
    };
  }
};
```

---

## STEP 3: Create All Pages

### 3.1 Page List

Based on `Requirement.md`, create ALL pages:

| Page | File | Description |
|------|------|-------------|
| Login | `src/views/Login.tsx` | User login |
| Register | `src/views/Register.tsx` | User registration |
| Dashboard | `src/views/Dashboard.tsx` | Main dashboard |
| ... | ... | ... |

### 3.2 Page Template

```tsx
// src/views/PageName.tsx
import { useState, useEffect } from 'react';
import { mockHandler } from '@/mocks/handlers/xxx';

export default function PageName() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Load mock data
    const result = mockHandler.getData();
    setData(result);
    setLoading(false);
  }, []);

  if (loading) return <div>Loading...</div>;

  return (
    <div className="page-name">
      {/* Page content using design system */}
    </div>
  );
}
```

---

## STEP 4: Apply Design System

### 4.1 CSS Variables

**`src/styles/variables.css`**
```css
:root {
  --color-primary: #XXXXXX;
  --color-secondary: #XXXXXX;
  --color-accent: #XXXXXX;
  --font-family: 'Inter', sans-serif;
  --spacing-unit: 8px;
  --border-radius: 8px;
}
```

### 4.2 Component Styles

Use design tokens consistently:
```css
.button-primary {
  background-color: var(--color-primary);
  color: white;
  padding: calc(var(--spacing-unit) * 2);
  border-radius: var(--border-radius);
}
```

---

## STEP 5: Verify Frontend Works

### 5.1 Check File Structure

```bash
ls -la src/views/
ls -la src/mocks/
ls -la src/components/
```

### 5.2 Run Frontend

```bash
npm install
npm run dev
```

### 5.3 Verify All Pages Load

- [ ] Login page loads at `/login`
- [ ] Register page loads at `/register`
- [ ] Dashboard loads at `/`
- [ ] All navigation works
- [ ] All mock data displays correctly

---

## ✅ COMPLETION CHECKPOINTS

**You CANNOT proceed to PHASE 2 until ALL checkpoints pass:**

| Checkpoint | Verification |
|------------|--------------|
| [ ] Design system documented | `cat src/design-system.md` |
| [ ] All pages exist | `ls src/views/` |
| [ ] Mock structure exists | `ls src/mocks/` |
| [ ] Frontend runs | `npm run dev` works |
| [ ] All pages load | Manual verification |
| [ ] QA Engineer approved | See QA report |
| [ ] User said "继续开发" | User input received |

---

## 🚫 DO NOT

- Do NOT write backend code
- Do NOT read `PHASE2-backend.md`
- Do NOT claim PHASE 1 complete until all checkpoints pass
- Do NOT skip design system

---

## 📞 GET HELP

If stuck:
1. Read `Requirement.md` again
2. Check design system documentation
3. Verify mock data structure matches requirements
