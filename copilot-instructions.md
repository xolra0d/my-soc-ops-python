# Copilot Instructions: Soc Ops Design Guide

This document provides design and implementation guidance for AI agents working on the Soc Ops frontend. It documents the **1980s-90s Arcade Aesthetic** redesign.

---

## 🎮 Design System Overview

**Soc Ops** uses a **retro neon arcade aesthetic** with dark backgrounds, bold neon colors, pixel-perfect borders, and snappy animations. This is purely visual—all game logic and functionality remain unchanged.

### Core Philosophy
- **Bold & Nostalgic**: Heavy use of neon colors and thick borders
- **Fast & Snappy**: Quick transitions (100ms), no smooth modern animations
- **High Contrast**: Dark backgrounds (#1a1a1a) with bright neon text
- **Arcade Vibes**: Chunky borders, glow effects, geometric styling

---

## 🎨 Color Palette

All colors use neon glow effects via `text-shadow` and `box-shadow`.

### Primary Colors
| Use | Hex | CSS Class | Effect |
|-----|-----|-----------|--------|
| Hot Pink (Primary CTA) | `#ff006e` | `.bg-accent` | Neon glow, strong contrast |
| Cyan (Secondary) | `#00f5ff` | `.text-gray-500` | Borders, accents |
| Lime Green (Success) | `#39ff14` | `.text-green-600`, `.bg-marked` | Winning states, highlights |
| Electric Purple | `#bf00ff` | — | Tertiary accents |
| Bright Yellow | `#ffff00` | `.text-amber-500` | Headings, strong text |
| Orange | `#ff6b35` | `.text-amber-800` | Warm accents |

### Background
| Use | Hex | CSS Class |
|-----|-----|-----------|
| Dark Base | `#1a1a1a` | — |
| Dark Elevated | `#2a2a2a` | `.bg-gray-100` |
| Scanlines | Overlay | `body` background-image |

### Application Rules
1. **Never use**: White (#ffffff), grays (#f9fafb), light backgrounds—they break the retro aesthetic
2. **Always pair colors with glow**: Text + `text-shadow`, elements + `box-shadow`
3. **Maintain contrast**: Lime/cyan text on #1a1a1a, yellow on #2a2a2a

---

## 🔤 Typography

### Fonts
- **Headlines** (`text-3xl` and up): `'Press Start 2P'`, cursive (imported from Google Fonts)
- **Body & UI** (text-sm, text-lg): `'Space Mono'`, monospace (imported from Google Fonts)
- **Fallback**: System monospace (`Courier New`, `Courier`)

### Usage Rules
| Element | Font | Size | Weight | Letter-Spacing |
|---------|------|------|--------|-----------------|
| Main title (h1) | Press Start 2P | text-5xl | 400 | 3px |
| Section title (h2) | Press Start 2P | text-4xl | 400 | 2px |
| Labels | Space Mono | text-lg | 700 | 2px |
| Body text | Space Mono | text-sm | 400 | 0px |

### Implementation
```html
<!-- Headline with neon glow -->
<h1 class="text-5xl text-amber-500" style="letter-spacing: 3px; text-shadow: 0 0 20px #ffff00, 0 0 40px #ff006e;">SOC OPS</h1>

<!-- Label with accent -->
<p class="text-lg text-green-600" style="letter-spacing: 2px; font-weight: 700;">▶ SOCIAL BINGO ◀</p>
```

---

## 🖼️ Visual Elements

### Borders
- **Thickness**: 3-4px (never thin borders)
- **Style**: Solid, always with neon glow
- **Color**: Match element purpose (pink for CTAs, cyan for secondary, green for success)

```css
/* Example */
border: 3px solid #ff006e;
box-shadow: 0 0 15px #ff006e;
```

### Glow Effects
Apply using `text-shadow` (text) and `box-shadow` (elements):

```css
/* Text glow */
text-shadow: 0 0 10px #ffff00, 0 0 20px #ff006e;

/* Element glow */
box-shadow: 0 0 20px #ff006e, 0 0 40px #00f5ff, inset 0 0 10px rgba(57, 255, 20, 0.2);
```

### Nesting & Depth
Create visual depth using nested bordered boxes:

```html
<!-- Double-border effect -->
<div style="border: 4px solid #ff006e; box-shadow: 0 0 20px #ff006e;">
  <div style="border: 2px solid #00f5ff; box-shadow: inset 0 0 10px rgba(0, 245, 255, 0.2);">
    Content here
  </div>
</div>
```

### Decorative Elements
- Replace modern icons with ASCII-style symbols: `▸ ◀ ◆ ▶ ◂ ◇ ✓`
- Use letter-spacing to create visual breathing room
- Add decorative lines for separation: `◆ ◇ ◆ ◇ ◆`

---

## 🎬 Animations & Transitions

### Timing
- **All transitions**: 100ms (snappy, not smooth)
- **Button press**: Instant depth shift (2px)
- **Glow pulse**: 1.5s infinite loop on modals/highlights

### Button Animations
```css
button {
    box-shadow: 0 0 15px #ff006e, inset 0 -4px 0 #ff006e;
}

button:hover {
    box-shadow: 0 0 25px #ff006e, 0 0 40px #00f5ff, inset 0 -4px 0 #ff006e;
    transform: translateY(-2px);
}

button:active {
    box-shadow: 0 0 15px #ff006e, inset 0 -2px 0 #ff006e, inset 0 2px 4px rgba(0,0,0,0.5);
    transform: translateY(2px);
}
```

### Glow Pulse Animation
```css
@keyframes neon-glow-pulse {
    0%, 100% {
        text-shadow: 0 0 10px #ff006e, 0 0 20px #00f5ff;
        box-shadow: 0 0 15px #ff006e, 0 0 30px #00f5ff;
    }
    50% {
        text-shadow: 0 0 20px #ff006e, 0 0 40px #00f5ff, 0 0 60px #39ff14;
        box-shadow: 0 0 25px #ff006e, 0 0 50px #00f5ff, inset 0 0 10px rgba(57, 255, 20, 0.3);
    }
}

.animate-neon-glow {
    animation: neon-glow-pulse 1.5s ease-in-out infinite;
}
```

---

## 📐 Layout Patterns

### Screen Structure
1. **Header**: Dark bg (#2a2a2a), cyan border, contains title and buttons
2. **Content Area**: Dark bg (#1a1a1a) with grid pattern overlay
3. **Game Board**: Bordered container with individual grid cells
4. **Modal**: Dark bg with triple neon glow effect, centered overlay

### Grid Spacing
- **Gap between cells**: 4px (visible, not tight)
- **Padding in containers**: 16px (1rem)
- **Padding on buttons**: 16px horizontal, 12px vertical

### Responsive Design
- Mobile: Full-width with padding adjustments
- Desktop: Centered max-width containers
- Text sizing stays consistent across breakpoints

---

## 🛠️ CSS Utilities Reference

### Color Classes (Updated for Retro)
```css
/* Backgrounds */
.bg-white              /* Dark neon border #1a1a1a + cyan border */
.bg-gray-50           /* Pure dark #1a1a1a */
.bg-gray-100          /* Elevated dark #2a2a2a */
.bg-accent            /* Hot pink #ff006e with glow */
.bg-marked            /* Lime green #39ff14 with glow */

/* Text Colors (all with glow) */
.text-white           /* White with glow */
.text-gray-500        /* Cyan */
.text-gray-600        /* Lime green */
.text-gray-700        /* Bright yellow */
.text-gray-800        /* Hot pink */
.text-gray-900        /* White with glow */
.text-green-600       /* Lime green with glow */
.text-amber-500       /* Bright yellow with glow */
.text-amber-800       /* Orange with glow */
```

### Border Classes
```css
.border               /* 3px solid pink with glow */
.border-b             /* 3px solid cyan with glow */
.border-gray-200      /* 3px cyan */
.border-gray-300      /* 3px lime */
.border-amber-400     /* 3px yellow */
.rounded              /* 0px (sharp corners) */
.rounded-lg           /* 2px minimal rounding */
.rounded-xl           /* 4px light rounding */
```

### Shadow/Glow Classes
```css
.shadow-sm            /* Light neon glow */
.shadow-xl            /* Heavy neon glow with inset */
```

---

## ✏️ Implementation Checklist

When creating new screens or components:

- [ ] Dark backgrounds (#1a1a1a or #2a2a2a)
- [ ] All text has `text-shadow` glow effect
- [ ] Borders are 3px+ with matching glow
- [ ] Use Press Start 2P for headlines (with letter-spacing)
- [ ] Use Space Mono for body text
- [ ] CTAs use hot pink (#ff006e) with yellow text
- [ ] Accents use cyan (#00f5ff) or lime (#39ff14)
- [ ] Buttons have depth effect (inset shadow)
- [ ] Hover/active states use enhanced glow
- [ ] Transitions are 100ms (snappy)
- [ ] Decorative elements use ASCII symbols
- [ ] Test on mobile and desktop

---

## 📝 Component Examples

### CTA Button
```html
<button
    style="
    background: #ff006e;
    border: 3px solid #ffff00;
    color: #ffff00;
    font-weight: 700;
    letter-spacing: 2px;
    padding: 1rem 1.5rem;
    text-shadow: 0 0 10px #ffff00;
    box-shadow: 0 0 25px #ff006e, inset 0 -4px 0 #ffff00;
    font-family: 'Space Mono', monospace;">
    ▶ START GAME ◀
</button>
```

### Info Card
```html
<div style="border: 4px solid #ff006e; box-shadow: 0 0 20px #ff006e;">
    <div style="border: 2px solid #00f5ff; background: #2a2a2a; padding: 1rem; box-shadow: inset 0 0 10px rgba(0, 245, 255, 0.2);">
        <h2 style="color: #ffff00; text-shadow: 0 0 10px #ffff00; letter-spacing: 2px;">TITLE</h2>
        <p style="color: #39ff14; text-shadow: 0 0 8px #39ff14;">Content with neon glow</p>
    </div>
</div>
```

### Game Board Cell
```html
<button
    style="
    border: 3px solid #ff006e;
    background: #1a1a1a;
    color: #ffff00;
    box-shadow: 0 0 10px #ff006e;
    text-shadow: 0 0 8px #ffff00;
    min-height: 60px;
    padding: 0.25rem;">
    Cell text
</button>

<!-- When marked -->
<button
    style="
    border: 3px solid #00f5ff;
    background: #2a2a2a;
    color: #39ff14;
    box-shadow: 0 0 15px #00f5ff, inset 0 0 8px rgba(0, 245, 255, 0.2);
    text-shadow: 0 0 8px #39ff14;
    min-height: 60px;
    padding: 0.25rem;">
    Cell text
</button>

<!-- When winning -->
<button
    style="
    border: 3px solid #ffff00;
    background: #39ff14;
    color: #1a1a1a;
    box-shadow: 0 0 20px #ffff00, inset 0 0 10px rgba(255, 255, 0, 0.3);
    text-shadow: 0 0 5px #1a1a1a;
    font-weight: 700;
    min-height: 60px;
    padding: 0.25rem;">
    Cell text
</button>
```

---

## 🚫 Anti-Patterns (Do NOT Do)

- ❌ Use light backgrounds or white
- ❌ Use modern, smooth transitions (keep snappy 100ms)
- ❌ Forget text-shadow on text elements
- ❌ Use thin borders (always 3px+)
- ❌ Mix in modern UI patterns (cards, rounded corners, soft shadows)
- ❌ Use emoji (use ASCII symbols instead)
- ❌ Apply glow to everything (be intentional)
- ❌ Use default fonts (always import Press Start 2P or Space Mono)

---

## 📚 Files to Reference

- **CSS**: `app/static/css/app.css` — Main stylesheet with all utilities
- **Start Screen**: `app/templates/components/start_screen.html` — Reference implementation
- **Game Screen**: `app/templates/components/game_screen.html` — Game board layout
- **Bingo Board**: `app/templates/components/bingo_board.html` — Grid cells styling
- **Win Modal**: `app/templates/components/bingo_modal.html` — Celebratory screen

---

## 🎯 Future Enhancements

If extending the retro aesthetic:
- Add CRT scanlines effect (CSS background pattern)
- Implement sound effects (retro arcade bleeps)
- Add alternative color themes (purple/magenta, blue/cyan)
- Create retro pixel animations
- Add typing effect on text reveal

---

*Last Updated: March 2026 | Designed for 1980s-90s Arcade Aesthetic*
