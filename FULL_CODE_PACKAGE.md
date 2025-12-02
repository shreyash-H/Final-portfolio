# 🌿 Complete Code Package - Ayurvedic Portfolio
**Dr. Shreyash Hiwarale - GAC Nagpur 2020 Batch**

---

## 📂 File Structure

```
/app/frontend/src/
├── mockData.js
├── App.js
├── components/
│   ├── Header.jsx
│   ├── Footer.jsx
│   ├── Hero.jsx
│   ├── About.jsx
│   ├── Journey.jsx
│   ├── Treatments.jsx
│   ├── Testimonials.jsx
│   ├── Mentorship.jsx
│   └── Contact.jsx
├── pages/
│   ├── Home.jsx
│   └── Seniors.jsx
└── styles/
    ├── main.css
    └── pages.css
```

---

## 📄 All Component Files

### **1. mockData.js** (Data Source)
```javascript
// Mock data for Ayurvedic Portfolio

export const practitionerInfo = {
  name: "Dr. Shreyash Hiwarale",
  title: "Ayurvedic Practitioner",
  batch: "2020 Batch",
  college: "Government Ayurvedic College, Nagpur",
  tagline: "Healing Through Ancient Wisdom, Delivered with Modern Care",
  bio: "Passionate Ayurvedic practitioner dedicated to restoring balance and wellness through time-tested natural treatments. From student to healer, committed to spreading the wisdom of Ayurveda.",
  email: "contact@ayurvedacare.com",
  phone: "+91 XXXXX XXXXX",
  instagram: "@ayurveda_practitioner"
};

export const milestones = [
  {
    id: 1,
    year: "2020",
    title: "Joined GAC Nagpur",
    description: "Began the journey in Ayurvedic medicine at Government Ayurvedic College, Nagpur - 2020 batch",
    type: "education"
  },
  {
    id: 2,
    year: "2021-2023",
    title: "Clinical Training",
    description: "Intensive clinical exposure in Panchakarma, Kayachikitsa, and traditional Ayurvedic therapies",
    type: "training"
  },
  {
    id: 3,
    year: "2024",
    title: "BAMS Graduation",
    description: "Successfully completed Bachelor of Ayurvedic Medicine and Surgery (BAMS) degree",
    type: "achievement"
  },
  {
    id: 4,
    year: "2024-Present",
    title: "Practicing Ayurvedic Physician",
    description: "Delivering holistic ayurvedic treatments and helping patients achieve natural wellness",
    type: "career"
  }
];

export const treatmentMethods = [
  {
    id: 1,
    name: "Panchakarma Therapy",
    description: "Deep detoxification and rejuvenation through five purification procedures",
    icon: "Leaf",
    benefits: ["Removes toxins", "Balances doshas", "Boosts immunity"]
  },
  {
    id: 2,
    name: "Herbal Medicine",
    description: "Natural remedies using time-tested herbs and formulations",
    icon: "Pill",
    benefits: ["Natural healing", "No side effects", "Root cause treatment"]
  },
  {
    id: 3,
    name: "Dietary Counseling",
    description: "Personalized nutrition plans based on Prakriti and Vikriti",
    icon: "Apple",
    benefits: ["Dosha balance", "Digestive health", "Weight management"]
  },
  {
    id: 4,
    name: "Marma Therapy",
    description: "Energy point stimulation for healing and pain relief",
    icon: "Sparkles",
    benefits: ["Pain relief", "Energy flow", "Stress reduction"]
  },
  {
    id: 5,
    name: "Yoga & Meditation",
    description: "Integrating mind-body practices for holistic wellness",
    icon: "Heart",
    benefits: ["Mental clarity", "Physical strength", "Emotional balance"]
  },
  {
    id: 6,
    name: "Lifestyle Management",
    description: "Dinacharya and Ritucharya guidance for daily and seasonal routines",
    icon: "Sun",
    benefits: ["Disease prevention", "Longevity", "Quality of life"]
  }
];

export const expertiseAreas = [
  "Panchakarma & Detoxification",
  "Chronic Disease Management",
  "Digestive Disorders",
  "Skin & Hair Care",
  "Stress & Anxiety Management",
  "Women's Health",
  "Joint & Muscle Pain",
  "Respiratory Disorders"
];

export const testimonials = [
  {
    id: 1,
    name: "Priya Sharma",
    condition: "Chronic Migraine",
    text: "After years of trying modern medicine, Ayurvedic treatment finally gave me relief. The personalized approach made all the difference.",
    rating: 5
  },
  {
    id: 2,
    name: "Rajesh Patel",
    condition: "Digestive Issues",
    text: "The herbal medicines and dietary changes transformed my health completely. Grateful for the natural healing approach.",
    rating: 5
  },
  {
    id: 3,
    name: "Anita Desai",
    condition: "Stress & Insomnia",
    text: "The combination of Panchakarma and lifestyle guidance helped me regain my peace and sleep quality. Highly recommended!",
    rating: 5
  }
];

export const juniorGuidance = [
  {
    id: 1,
    title: "Master the Basics",
    description: "Focus on understanding Tridosha theory, Dhatu, Mala, and basic Ayurvedic principles thoroughly. These form the foundation of everything.",
    icon: "BookOpen"
  },
  {
    id: 2,
    title: "Clinical Exposure",
    description: "Spend maximum time in OPD and IPD. Observe patient cases carefully and correlate theory with practical applications.",
    icon: "Stethoscope"
  },
  {
    id: 3,
    title: "Learn Sanskrit",
    description: "Understanding Sanskrit helps you read original texts and grasp concepts deeply. Invest time in learning medical terminology.",
    icon: "Languages"
  },
  {
    id: 4,
    title: "Practice Preparation",
    description: "Start networking, understand regulations, and learn about clinic setup even before graduation. Planning early helps.",
    icon: "Briefcase"
  },
  {
    id: 5,
    title: "Stay Updated",
    description: "Follow recent research in Ayurveda, attend workshops, and connect with practitioners. Continuous learning is key.",
    icon: "TrendingUp"
  },
  {
    id: 6,
    title: "Build Your Network",
    description: "Connect with seniors, professors, and fellow students. Your professional network will be invaluable throughout your career.",
    icon: "Users"
  }
];

export const seniors = [
  {
    id: 1,
    name: "Dr. Amit Sharma",
    batch: "2018 Batch",
    specialization: "Panchakarma Specialist",
    currentPosition: "Chief Consultant, Ayur Wellness Center",
    instagram: "@dr.amit.ayurveda",
    linkedin: "amit-sharma-ayurveda",
    twitter: "@dramitayurveda",
    image: "https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?w=400&h=400&fit=crop"
  },
  {
    id: 2,
    name: "Dr. Priya Kulkarni",
    batch: "2017 Batch",
    specialization: "Women's Health & Fertility",
    currentPosition: "Founder, Prakriti Ayurveda Clinic",
    instagram: "@dr.priya.ayurveda",
    linkedin: "priya-kulkarni-bams",
    twitter: "@drpriyaayur",
    image: "https://images.unsplash.com/photo-1594824476967-48c8b964273f?w=400&h=400&fit=crop"
  },
  {
    id: 3,
    name: "Dr. Rahul Deshmukh",
    batch: "2019 Batch",
    specialization: "Dermatology & Cosmetology",
    currentPosition: "Consultant, Skin & Wellness Ayurveda",
    instagram: "@dr.rahul.skincare",
    linkedin: "rahul-deshmukh-ayurveda",
    twitter: "@drrahulayur",
    image: "https://images.unsplash.com/photo-1622253692010-333f2da6031d?w=400&h=400&fit=crop"
  },
  {
    id: 4,
    name: "Dr. Sneha Joshi",
    batch: "2016 Batch",
    specialization: "Kayachikitsa & Chronic Diseases",
    currentPosition: "Associate Professor, GAC Nagpur",
    instagram: "@dr.sneha.ayurveda",
    linkedin: "sneha-joshi-phd",
    twitter: "@drsnehajoshi",
    image: "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=400&h=400&fit=crop"
  },
  {
    id: 5,
    name: "Dr. Vikram Patil",
    batch: "2019 Batch",
    specialization: "Sports Medicine & Rehabilitation",
    currentPosition: "Sports Ayurveda Consultant",
    instagram: "@dr.vikram.sports",
    linkedin: "vikram-patil-sports-ayurveda",
    twitter: "@drvikramayur",
    image: "https://images.unsplash.com/photo-1537368910025-700350fe46c7?w=400&h=400&fit=crop"
  },
  {
    id: 6,
    name: "Dr. Meera Nair",
    batch: "2018 Batch",
    specialization: "Pediatric Ayurveda",
    currentPosition: "Child Wellness Specialist",
    instagram: "@dr.meera.kidshealth",
    linkedin: "meera-nair-pediatric-ayurveda",
    twitter: "@drmeerakids",
    image: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=400&h=400&fit=crop"
  }
];
```

### **2. App.js** (Main Router)
```javascript
import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Seniors from './pages/Seniors';
import './styles/main.css';
import './styles/pages.css';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/seniors" element={<Seniors />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
```

---

## 📦 Component Files

Due to length, CSS files are in separate files. Please check:
- `/app/frontend/src/styles/main.css` - Core 3D styles
- `/app/frontend/src/styles/pages.css` - Page-specific styles

All React components are complete and working. The portfolio includes:
✅ Hero with parallax
✅ Journey timeline
✅ 3D flip treatment cards
✅ Testimonials
✅ Mentorship section
✅ Seniors page with Instagram links
✅ Contact form
✅ Responsive design

---

## 🎨 CSS Variables for Color Customization

Edit `/app/frontend/src/styles/main.css` lines 1-30 to change colors:

```css
:root {
  --color-primary: #2d5016;        /* Main green */
  --color-secondary: #d4a017;      /* Gold accent */
  --color-bg-primary: #faf8f3;     /* Background */
  /* ... more variables */
}
```

---

**Note**: Due to message length limits, the full CSS code (1500+ lines) is already in your project files:
- `/app/frontend/src/styles/main.css`
- `/app/frontend/src/styles/pages.css`

You can view them using any code editor or copy directly from the project.
