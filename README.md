# 📧 Email Finder | Designed by YogSec

## 📝 Overview
Email Finder is a powerful and fast Python-based tool designed to extract email addresses from websites. It helps security researchers, penetration testers, and web analysts quickly discover contact information from target websites by scanning common contact endpoints.

## 🌟 Features
- 🧑‍💻 Multi-threaded for fast email extraction
- 📄 Supports scanning single URLs or a list of URLs
- 💾 Option to save extracted emails to a file
- 🆘 Help menu for usage guidance
- 🏷️ Version display functionality

## 🚀 Installation
```bash
git clone https://github.com/YogSec/email-finder.git
cd email-finder
pip install -r requirements.txt
```

## 🛠️ Usage
```bash
python email_finder.py -h
```
### Scan a Single Domain
```bash
python email_finder.py -d https://example.com
```
### Scan Multiple Domains from a File
```bash
python email_finder.py -l urls.txt
```
### Save Output to a File
```bash
python email_finder.py -d https://example.com -s output.txt
```
### Show Version
```bash
python email_finder.py -v
```
## 📂 Expected Output
Example output from the tool:
```bash
support@example.com
contact@example.com
admin@example.com
```
## 🔍 How It Works
- The tool checks the main page and common contact-related endpoints like `/contact-us`, `/about`, `/support`, `/team`, etc.
- Extracts all email addresses found in the HTML content.
- Uses multi-threading for concurrent processing of multiple pages, ensuring speed and efficiency.

## 🔗 Common Endpoints Checked
- `/contact-us`
- `/contact`
- `/about`
- `/support`
- `/help`
- `/team`
- `/careers`
- `/jobs`
- `/faq`
- `/press`
- `/media`
- `/partners`
- `/company`
- `/privacy-policy`
- `/terms`
- `/legal`
- `/get-in-touch`
- `/reach-us`
- `/enquiries`
- `/feedback`
- `/customer-support`
- `/customer-service`
- `/connect`
- `/who-we-are`
- `/meet-the-team`
- `/en/contact`
- `/en/about`
- `/en/support`
- `/info/contact`
- `/company/contact`

## ⚠️ Disclaimer
This tool is designed for educational and ethical purposes only. Ensure you have proper authorization before scanning any website.

## 🧑‍💻 Author
Developed by YogSec

## 🌍 License
This project is licensed under the MIT License.

## 🌟 Let's Connect!

Hello, Hacker! 👋 We'd love to stay connected with you. Reach out to us on any of these platforms and let's build something amazing together:

🌐 **Website:** [https://yogsec.github.io/yogsec/](https://yogsec.github.io/yogsec/)  
📜 **Linktree:** [https://linktr.ee/yogsec](https://linktr.ee/yogsec)  
🔗 **GitHub:** [https://github.com/yogsec](https://github.com/yogsec)  
💼 **LinkedIn (Company):** [https://www.linkedin.com/company/yogsec/](https://www.linkedin.com/company/yogsec/)  
📷 **Instagram:** [https://www.instagram.com/yogsec.io/](https://www.instagram.com/yogsec.io/)  
🐦 **Twitter (X):** [https://x.com/yogsec](https://x.com/yogsec)  
👨‍💼 **Personal LinkedIn:** [https://www.linkedin.com/in/bug-bounty-hunter/](https://www.linkedin.com/in/bug-bounty-hunter/)  
📧 **Email:** abhinavsingwal@gmail.com

---

## ☕ Buy Me a Coffee

If you find our work helpful and would like to support us, consider buying us a coffee. Your support keeps us motivated and helps us create more awesome content. ❤️

☕ **Support Us Here:** [https://buymeacoffee.com/yogsec](https://buymeacoffee.com/yogsec)
