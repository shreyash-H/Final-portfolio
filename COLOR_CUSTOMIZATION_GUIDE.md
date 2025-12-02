# 🎨 Color Customization Guide

Your Ayurvedic Portfolio website uses CSS variables for easy color customization. All colors can be changed in one place!

## 📍 Where to Edit Colors

Open this file: `/app/frontend/src/styles/main.css`

Look for the `:root` section at the top (lines 1-30). All editable colors are defined there.

## 🌿 Current Color Scheme (Earthy & Natural)

```css
:root {
  /* Primary Colors - Deep Forest Green */
  --color-primary: #2d5016;         /* Main brand color - buttons, headings */
  --color-primary-light: #4a7c2c;   /* Lighter shade for hover effects */
  --color-primary-dark: #1a3009;    /* Darker shade for footer */
  
  /* Secondary Colors - Golden */
  --color-secondary: #d4a017;       /* Gold accents - subtitle, badges */
  --color-secondary-light: #f0c645; /* Lighter gold */
  --color-secondary-dark: #a67c00;  /* Darker gold */
  
  /* Accent Colors - Brown */
  --color-accent: #8b4513;          /* Accent elements */
  --color-accent-light: #a0522d;    /* Lighter accent */
  
  /* Background Colors */
  --color-bg-primary: #faf8f3;      /* Main page background */
  --color-bg-secondary: #f5f1e8;    /* Section backgrounds */
  --color-bg-tertiary: #eae5d8;     /* Card backgrounds */
  
  /* Text Colors */
  --color-text-primary: #2c2416;    /* Main text */
  --color-text-secondary: #5a5343;  /* Secondary text */
  --color-text-muted: #87826f;      /* Muted/subtle text */
  
  /* White & Grays */
  --color-white: #ffffff;
  --color-gray-100: #f7f7f7;
  --color-gray-200: #e5e5e5;
}
```

## 🎨 Alternative Color Palettes You Can Try

### Option 1: Modern Blue (Professional Medical)
```css
--color-primary: #1e3a8a;         /* Deep blue */
--color-primary-light: #3b82f6;   /* Bright blue */
--color-primary-dark: #1e293b;    /* Navy */
--color-secondary: #10b981;       /* Emerald green */
--color-bg-primary: #f8fafc;      /* Light gray-blue */
```

### Option 2: Warm Orange (Energetic & Welcoming)
```css
--color-primary: #c2410c;         /* Burnt orange */
--color-primary-light: #f97316;   /* Orange */
--color-primary-dark: #7c2d12;    /* Dark orange */
--color-secondary: #fbbf24;       /* Amber */
--color-bg-primary: #fffbeb;      /* Warm cream */
```

### Option 3: Purple (Spiritual & Healing)
```css
--color-primary: #6b21a8;         /* Deep purple */
--color-primary-light: #a855f7;   /* Purple */
--color-primary-dark: #4c1d95;    /* Dark purple */
--color-secondary: #ec4899;       /* Pink accent */
--color-bg-primary: #faf5ff;      /* Light purple tint */
```

### Option 4: Teal (Calm & Healing)
```css
--color-primary: #0f766e;         /* Teal */
--color-primary-light: #14b8a6;   /* Light teal */
--color-primary-dark: #134e4a;    /* Dark teal */
--color-secondary: #f59e0b;       /* Amber */
--color-bg-primary: #f0fdfa;      /* Mint tint */
```

### Option 5: Monochrome (Elegant & Minimalist)
```css
--color-primary: #18181b;         /* Almost black */
--color-primary-light: #3f3f46;   /* Dark gray */
--color-primary-dark: #09090b;    /* Pure black */
--color-secondary: #71717a;       /* Medium gray */
--color-bg-primary: #fafafa;      /* Off-white */
```

## 🔧 How to Change Colors

1. **Choose a palette** from the options above (or create your own!)

2. **Open the file**: `/app/frontend/src/styles/main.css`

3. **Replace the color values** in the `:root` section

4. **Save the file** - the website will automatically reload with new colors!

## 💡 Pro Tips

- **Use a color picker tool** like [Coolors.co](https://coolors.co/) or [Adobe Color](https://color.adobe.com/) to generate harmonious color schemes

- **Test contrast**: Make sure text colors have enough contrast with backgrounds for readability

- **Keep consistency**: 
  - Primary = Main brand color (buttons, headings)
  - Secondary = Accent color (highlights, badges)
  - Background = Neutral, calming tones

- **For medical/Ayurveda themes**: 
  - Greens = Nature, healing
  - Blues = Trust, professionalism
  - Purples = Spirituality, holistic
  - Earthy tones = Natural, grounded

## 🎯 Quick Color Test

After changing colors, check these elements:
- ✅ Hero section title and buttons
- ✅ Navigation links on hover
- ✅ Timeline icons and cards
- ✅ Treatment cards (flip them!)
- ✅ Form inputs and submit button
- ✅ Footer readability

## 🆘 Need Help?

If colors don't look right:
1. Make sure you saved the file
2. Check browser console (F12) for errors
3. Clear browser cache (Ctrl+F5 / Cmd+Shift+R)
4. Restart frontend: `sudo supervisorctl restart frontend`

---

**Current Theme**: Earthy Natural (Green & Gold)
**File Location**: `/app/frontend/src/styles/main.css`
**Lines to Edit**: 1-30 (`:root` section)
