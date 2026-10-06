<div align="center">

<img src="assets/branding/logos/logo.png" alt="UnnoyonOS Logo" width="120" height="120" style="border-radius: 50%;" />

# UnnoyonOS

**A professional, macOS-inspired Debian-based Linux distribution with KDE Plasma**

[![License](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](LICENSE)
[![Base](https://img.shields.io/badge/Base-Debian%20Trixie-red.svg)](https://www.debian.org/)
[![Desktop](https://img.shields.io/badge/Desktop-KDE%20Plasma-blue.svg)](https://kde.org/)
[![Status](https://img.shields.io/badge/Status-In%20Development-yellow.svg)]()

</div>

---

## 📖 About

**UnnoyonOS** is a custom Debian-based Linux distribution built with `live-build`, featuring a polished **KDE Plasma** desktop environment designed to deliver a premium, macOS-like user experience. The goal is a beautiful, fast, and professional OS for everyday use and development.

### ✨ Key Features
- 🎨 **macOS-inspired** design with custom KDE Plasma theme
- 🚀 **Debian Trixie** base for stability and cutting-edge packages
- 💎 **KDE Plasma** desktop — powerful and fully customizable
- 🔧 **live-build** powered ISO creation pipeline
- 📦 Curated software selection for productivity & development

---

## 🏗️ Project Structure

```
UnnoyonOS-Dev/
├── UnnoyonOS/              # Main live-build project
│   ├── config/             # live-build configuration
│   │   ├── binary          # ISO/binary stage settings
│   │   ├── bootstrap       # Base system settings
│   │   ├── chroot          # Chroot stage settings
│   │   ├── package-lists/  # Packages to install
│   │   ├── hooks/          # Custom build hooks
│   │   ├── includes.chroot/# Files to copy into the live system
│   │   └── preseed/        # Installer preseed answers
│   └── auto/               # live-build auto scripts
├── assets/                 # Branding & visual assets
│   └── branding/
│       ├── logos/          # OS logos
│       └── wallpapers/     # Default wallpapers
├── plasma-workspace/       # KDE Plasma workspace customizations
├── dolphin/                # Dolphin file manager customizations
└── docs/                   # Documentation
```

---

## 🛠️ Build Requirements (Linux only)

> ⚠️ **Building must be done on a Linux system.** ISO creation does not work on Windows.

### Prerequisites
```bash
sudo apt update
sudo apt install live-build git curl wget
```

### Clone the Repository
```bash
git clone https://github.com/Veldora/UnnoyonOS.git
cd UnnoyonOS/UnnoyonOS
```

### Build the ISO
```bash
# Initialize live-build
lb config

# Build the ISO (requires root / sudo)
sudo lb build 2>&1 | tee build.log
```

The resulting ISO will be in the project root as `live-image-amd64.hybrid.iso`.

---

## 🔥 Quick Build Script

```bash
cd UnnoyonOS
sudo lb clean --all
sudo lb build 2>&1 | tee build.log
```

---

## 📋 Roadmap

- [ ] Custom KDE theme (macOS-inspired)
- [ ] Custom SDDM login screen
- [ ] Custom Plymouth boot splash
- [ ] App store / software center integration
- [ ] Custom installer (Calamares)
- [ ] Custom wallpapers & icon theme
- [ ] Bengali language support
- [ ] First-run setup wizard
- [ ] System update manager

---

## 🤝 Contributing

This project is in active development. Contributions, ideas, and feedback are welcome!

---

## 📄 License

This project is licensed under the **GPL-3.0 License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">
Made with ❤️ by the UnnoyonOS Team
</div>
