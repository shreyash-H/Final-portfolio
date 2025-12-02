# 🌿 Ayurvedic Practitioner Portfolio - 3D Modern Design

A stunning portfolio website showcasing your journey from student (GAC Nagpur 2020 batch) to Ayurvedic Practitioner, with mentorship guidance for juniors and a seniors directory with social links.

## ✨ Features Implemented

### 🏠 Main Portfolio (Home Page)

1. **Hero Section**
   - Full-screen introduction with parallax floating leaf elements
   - 2020 Batch badge, name, title, and tagline
   - Two CTA buttons: "Explore Treatments" and "Book Consultation"
   - Smooth scroll indicator

2. **About Section**
   - 3D rotatable image placeholder (add your photo later)
   - Professional bio highlighting your Ayurvedic journey
   - 8 Areas of Expertise tags with hover effects

3. **Journey Timeline**
   - Interactive vertical timeline with 3D depth effects
   - 4 Major milestones:
     - 2020: Joined GAC Nagpur
     - 2021-2023: Clinical Training
     - 2024: BAMS Graduation
     - 2024-Present: Practicing Physician
   - Color-coded icons for different milestone types

4. **Treatment Methods Section**
   - 6 Treatment cards with **3D flip animation**
   - Front: Icon, name, description
   - Back: Benefits list (flip on hover!)
   - Methods covered:
     - Panchakarma Therapy
     - Herbal Medicine
     - Dietary Counseling
     - Marma Therapy
     - Yoga & Meditation
     - Lifestyle Management

5. **Patient Testimonials**
   - 3 Testimonial cards with hover effects
   - Star ratings, patient names, and conditions treated
   - Realistic testimonial content

6. **Mentorship Section**
   - 6 Guidance cards for junior Ayurvedic students
   - Topics: Basics, Clinical exposure, Sanskrit, Practice prep, Updates, Networking
   - **"Meet Your Seniors" CTA button** → Links to Seniors page

7. **Contact Section**
   - Contact information display (email, phone, Instagram, location)
   - Functional contact form (demo mode - shows alert on submit)
   - Professional styling with focus states

8. **Header & Footer**
   - Sticky header with smooth scroll navigation
   - Responsive mobile menu
   - Footer with quick links and contact info

### 👥 Seniors Directory Page

9. **Seniors Social Network Page**
   - Dedicated page showing 6 GAC Nagpur alumni/seniors
   - Each senior card displays:
     - Professional photo
     - Name, batch year
     - Specialization
     - Current position
     - **Instagram link (prominently featured)**
     - LinkedIn & Twitter links
   - Cards with 3D hover effects
   - "Back to Home" navigation button

## 🎨 Design Features

### Modern 3D Elements
- ✅ **3D Card Flips**: Treatment cards rotate 180° on hover
- ✅ **3D Transforms**: Timeline cards, senior cards have depth effects
- ✅ **Parallax Scrolling**: Floating leaves in hero section move at different speeds
- ✅ **Perspective Effects**: About section image has 3D rotation
- ✅ **Depth Shadows**: Multiple shadow layers create depth
- ✅ **Smooth Animations**: Fade-ins, slide-ups, hover transitions

### Color System (Fully Editable!)
- **Primary**: Deep forest green (#2d5016) - Ayurvedic/Nature theme
- **Secondary**: Golden (#d4a017) - Traditional warmth
- **Accent**: Saddle brown - Grounding
- **Backgrounds**: Warm cream tones
- **All colors editable via CSS variables** - See `COLOR_CUSTOMIZATION_GUIDE.md`

### Responsive Design
- ✅ Mobile-friendly (320px+)
- ✅ Tablet optimized (768px+)
- ✅ Desktop enhanced (1024px+)
- ✅ Mobile menu with slide-down animation

## 📁 Project Structure

```
/app/frontend/src/
├── components/
│   ├── Header.jsx          # Navigation with smooth scroll
│   ├── Footer.jsx          # Footer with links
│   ├── Hero.jsx            # Hero with parallax effects
│   ├── About.jsx           # About with 3D image
│   ├── Journey.jsx         # Timeline component
│   ├── Treatments.jsx      # 3D flip cards
│   ├── Testimonials.jsx    # Patient reviews
│   ├── Mentorship.jsx      # Junior guidance + CTA
│   └── Contact.jsx         # Contact form
├── pages/
│   ├── Home.jsx            # Main portfolio page
│   └── Seniors.jsx         # Seniors directory page
├── styles/
│   ├── main.css            # Core styles + 3D effects + CSS variables
│   └── pages.css           # Page-specific styles
├── mockData.js             # All placeholder data
└── App.js                  # Routes setup
```

## 🚀 Current Status

### ✅ Completed (Frontend-only with Mock Data)
- All 9 sections fully implemented
- 3D animations and effects working
- Responsive design complete
- Navigation and routing functional
- Color system with CSS variables
- Seniors page with Instagram links

### 📝 Placeholder Content
The following content uses mock data that you can easily update:

1. **Personal Info** (`mockData.js` - `practitionerInfo`)
   - Replace `"Dr. [Your Name]"` with your actual name
   - Update email, phone, Instagram handle

2. **Milestones** (`mockData.js` - `milestones`)
   - Timeline is pre-filled with GAC Nagpur 2020 batch journey
   - Add more specific achievements if needed

3. **Testimonials** (`mockData.js` - `testimonials`)
   - 3 placeholder testimonials included
   - Replace with real patient reviews

4. **Seniors Data** (`mockData.js` - `seniors`)
   - 6 placeholder seniors with realistic names and roles
   - **Update with actual GAC Nagpur seniors' info**
   - **Replace Instagram handles with real ones**
   - Update LinkedIn and Twitter usernames
   - Replace placeholder images with real photos

5. **About Section Photo**
   - Currently shows green gradient placeholder
   - Replace with your professional photo

## 🎨 How to Customize Colors

**See detailed guide**: `/app/COLOR_CUSTOMIZATION_GUIDE.md`

**Quick start**:
1. Open `/app/frontend/src/styles/main.css`
2. Edit color values in `:root` section (lines 1-30)
3. Save file - website auto-reloads!

Pre-made color palettes available in the guide:
- Current: Earthy Natural (Green & Gold)
- Option 1: Modern Blue (Professional Medical)
- Option 2: Warm Orange (Energetic)
- Option 3: Purple (Spiritual)
- Option 4: Teal (Calm)
- Option 5: Monochrome (Elegant)

## 🔄 Next Steps (Optional Backend Integration)

Currently, the website is fully functional with **frontend-only** features:
- All interactions work (buttons, forms, navigation)
- Data is stored in browser (temporary)
- Contact form shows alert (not sent to email)

**If you want to add backend features later:**
1. Save contact form submissions to database
2. Dynamic content management
3. Email notifications
4. Admin panel for updating content
5. Real patient testimonials system

**For now, you can use the website as-is and manually update content in `mockData.js`!**

## 📱 How to Update Content

### Update Your Personal Info
Edit `/app/frontend/src/mockData.js`:
```javascript
export const practitionerInfo = {
  name: "Dr. Rahul Sharma",  // Your name here
  email: "rahul@example.com",
  phone: "+91 98765 43210",
  instagram: "@dr.rahul.ayurveda"
};
```

### Update Seniors List
Edit `/app/frontend/src/mockData.js`:
```javascript
export const seniors = [
  {
    name: "Dr. Actual Senior Name",
    batch: "2018 Batch",
    specialization: "Their specialization",
    instagram: "@their.real.instagram",
    linkedin: "their-linkedin-username",
    image: "URL to their photo"
  },
  // Add more seniors...
];
```

### Add Your Photo
Replace the placeholder in About section:
1. Upload your photo to `/app/frontend/public/images/`
2. Edit `/app/frontend/src/components/About.jsx`
3. Replace the `.about-image-placeholder` div with:
```jsx
<img src="/images/your-photo.jpg" alt="Your Name" />
```

## 🌐 Website URLs

- **Home Page**: `http://localhost:3000/`
- **Seniors Page**: `http://localhost:3000/seniors`

## 🎯 Key Features for Juniors

The website helps juniors in two ways:

1. **Mentorship Guidance Section**
   - 6 Essential tips for BAMS students
   - Career preparation advice
   - Study strategies

2. **Seniors Directory**
   - **Direct access to seniors' Instagram accounts**
   - See specializations and career paths
   - Connect via LinkedIn and Twitter
   - Learn from their journey

## 💡 Tips for Using This Portfolio

1. **Update mock data first** before showing to anyone
2. **Add your real photo** to the About section
3. **Get real testimonials** from patients (with permission)
4. **Customize colors** to match your brand
5. **Update seniors list** with actual GAC Nagpur alumni who agree to be listed
6. **Test on mobile** - it's fully responsive!

## 🆘 Need Help?

**Restart services:**
```bash
sudo supervisorctl restart frontend
```

**Check if running:**
```bash
sudo supervisorctl status
```

**View logs:**
```bash
tail -f /var/log/supervisor/frontend.*.log
```

## 📋 Summary

✅ **Complete 3D portfolio website** with modern design
✅ **Journey showcase** from 2020 batch to practitioner  
✅ **Treatment methods** with interactive 3D cards
✅ **Junior mentorship** guidance section
✅ **Seniors directory** page with Instagram + social links
✅ **Editable color system** via CSS variables
✅ **Fully responsive** design
✅ **Ready to use** with mock data
✅ **No backend needed** for now (all frontend features work!)

---

**Built with**: React, React Router, Lucide Icons, CSS3 3D Transforms
**Theme**: Ayurvedic / Natural / Professional
**Status**: ✅ Frontend Complete with Mock Data
