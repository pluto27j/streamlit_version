"""
Curated ATS-Compliant Resume Templates for various tech domains.
Formatted in clean Markdown & plain text ready for preview and instant download.
"""

RESUME_TEMPLATES = {
    "Software & Full Stack Engineer (ATS High-Impact)": {
        "domain": "Software Engineering",
        "desc": "Optimized for software engineers, frontend, backend, and full-stack roles targeting high-growth tech companies.",
        "content": """# FIRSTNAME LASTNAME
Bengaluru, India | +91 98765 43210 | email@example.com | linkedin.com/in/yourprofile | github.com/yourusername

---

### PROFESSIONAL SUMMARY
Results-driven Full Stack Software Engineer with 3+ years of experience building high-throughput web applications, microservices, and distributed systems. Proven track record in reducing API latency by 35% and delivering resilient software serving 500K+ monthly active users using React, Node.js, and PostgreSQL.

---

### TECHNICAL SKILLS
- **Languages:** JavaScript (ES6+), TypeScript, Python, SQL, HTML5, CSS3
- **Frontend:** React.js, Next.js, Redux Toolkit, Tailwind CSS, Responsive Web Design
- **Backend & APIs:** Node.js, Express.js, FastAPI, RESTful APIs, GraphQL, WebSockets
- **Databases & Caching:** PostgreSQL, MySQL, MongoDB, Redis
- **Cloud & DevOps:** Docker, AWS (S3, EC2, Lambda), Git, GitHub Actions, CI/CD
- **Testing & Tools:** Jest, React Testing Library, Postman, Vite, Linux CLI

---

### PROFESSIONAL EXPERIENCE
**Software Engineer** | TechSolutions India Pvt Ltd, Bengaluru  
*July 2023 – Present*
- Architected and delivered a multi-tenant client portal using Next.js and PostgreSQL, increasing client adoption by 40%.
- Engineered asynchronous worker queues using Redis and BullMQ, reducing core checkout latency from 1.8s to 420ms.
- Implemented robust unit and integration testing pipelines with Jest, maintaining 88%+ code coverage across 40+ microservices.
- Collaborated in cross-functional Agile sprints, resolving 120+ customer-facing issues within SLA boundaries.

**Associate Software Engineer** | Innovate Labs, Hyderabad  
*August 2021 – June 2023*
- Developed 25+ reusable responsive UI components in React and Tailwind CSS compliant with WCAG 2.1 AA accessibility standards.
- Designed relational schemas and indexed queries in PostgreSQL, eliminating N+1 database bottlenecks.
- Spearheaded migration from legacy monolithic scripts to containerized Docker microservices deployed on AWS EC2.

---

### NOTABLE PROJECTS
**Real-Time Collaborative Code & Markdown Editor** | *Next.js, WebSockets, Redis, Tailwind CSS*
- Built real-time collaborative workspace supporting live cursor synchronization and concurrent document editing.
- Implemented operational transform algorithms with Redis Pub/Sub, handling 1,000+ concurrent active socket connections.
- Integrated syntax-highlighting engine and one-click PDF export feature with zero render delay.

**High-Throughput E-Commerce Inventory & Order API** | *FastAPI, PostgreSQL, Redis, Docker*
- Engineered transactional inventory reservation engine with atomic ACID compliance under heavy flash-sale loads.
- Designed comprehensive OpenAPI Swagger documentation and automated test suites with Pytest.

---

### EDUCATION
**Bachelor of Technology in Computer Science & Engineering**  
National Institute of Technology, India | *Graduated: 2021* | CGPA: 8.7 / 10.0

---

### CERTIFICATIONS
- AWS Certified Developer – Associate (2024)
- Meta Front-End Developer Professional Certificate (2023)
"""
    },

    "AI & Data Science Specialist (Research & MLOps)": {
        "domain": "AI & Data Science",
        "desc": "Tailored for AI Engineers, Machine Learning Practitioners, and Data Scientists highlighting model metrics and business impact.",
        "content": """# FIRSTNAME LASTNAME
Hyderabad, India | +91 91234 56789 | data.specialist@example.com | linkedin.com/in/yourprofile | kaggle.com/yourprofile

---

### PROFESSIONAL SUMMARY
Analytical AI and Machine Learning Engineer with strong foundations in statistical modeling, Deep Learning, and Retrieval-Augmented Generation (RAG). Experienced in training and deploying production ML systems on cloud infrastructure, achieving 94% precision on classification tasks and driving quantifiable business decision-making.

---

### TECHNICAL COMPETENCIES
- **Machine Learning:** Supervised/Unsupervised Learning, Random Forests, XGBoost, Scikit-Learn
- **Deep Learning & GenAI:** PyTorch, TensorFlow, Transformers, Hugging Face, LangChain, RAG, ChromaDB
- **Data Engineering & Analytics:** Python, Pandas, NumPy, SQL, Apache Spark, Airflow
- **Visualization & BI:** Tableau, Power BI, Seaborn, Matplotlib, Streamlit
- **MLOps & Deployment:** Docker, FastAPI, MLflow, AWS S3, ONNX Runtime, Git

---

### PROFESSIONAL EXPERIENCE
**Machine Learning Engineer** | DataMinds AI Solutions, Bengaluru  
*January 2023 – Present*
- Designed and deployed an enterprise Retrieval-Augmented Generation (RAG) assistant over 100K+ legal PDFs using LangChain and Pinecone.
- Developed predictive customer churn classifier in XGBoost, saving an estimated ₹45 Lakhs in annual customer churn.
- Implemented automated data drift detection pipelines using MLflow, triggering automated model retraining when PSI > 0.2.
- Reduced model inference latency by 60% through INT8 quantization and ONNX runtime optimizations.

**Data Analyst** | Analytics Global Corp, Pune  
*June 2021 – December 2022*
- Analyzed 5M+ daily transaction logs using PostgreSQL and Apache Spark to identify fraud trends.
- Built 15+ automated executive KPI dashboards in Power BI, adopted across product and finance divisions.
- Conducted hypothesis testing and A/B test power analysis for new checkout flow iterations.

---

### FEATURED PROJECTS
**Autonomous Document Intelligence & Summarizer Agent** | *PyTorch, LangGraph, Streamlit, ChromaDB*
- Implemented multi-step agentic workflow capable of extracting tables, key-value pairs, and executive summaries from unstructured contracts.
- Ranked in the top 5% of open-source GenAI tools with 400+ GitHub stars.

**Medical Imaging Multi-Class Pathology Classifier** | *PyTorch, Torchvision, Albumentations*
- Trained DenseNet-121 on 80,000 chest X-ray images, achieving 0.92 ROC-AUC score across 14 pathology labels.
- Implemented Grad-CAM attention heatmap overlays to assist radiologists in visual model verification.

---

### EDUCATION
**B.Tech / M.Tech in Artificial Intelligence & Data Science**  
Indian Institute of Information Technology | *2021*

---

### AWARDS & CERTIFICATIONS
- DeepLearning.AI Machine Learning Specialization (Andrew Ng)
- Kaggle Competitions Expert (Top 2% Globally)
"""
    },

    "Cloud & DevOps Engineer (Infrastructure as Code)": {
        "domain": "Cloud & DevOps",
        "desc": "Built for DevOps Engineers, Site Reliability Engineers, and Cloud Architects emphasizing 99.99% uptime and automation.",
        "content": """# FIRSTNAME LASTNAME
Pune, India | +91 99887 76655 | devops.pro@example.com | linkedin.com/in/yourprofile | github.com/yourusername

---

### PROFESSIONAL SUMMARY
Site Reliability and DevOps Engineer with 4+ years of expertise managing cloud infrastructure on AWS, building automated CI/CD deployment pipelines, and scaling Kubernetes microservices clusters. Champion of Infrastructure-as-Code (Terraform) and GitOps practices, maintaining 99.98% platform uptime SLAs.

---

### CORE SKILLS
- **Cloud Providers:** Amazon Web Services (AWS - VPC, EC2, EKS, RDS, S3, IAM, CloudWatch)
- **Containerization & Orchestration:** Docker, Kubernetes (EKS), Helm, Containerd
- **Infrastructure as Code:** Terraform, Ansible, CloudFormation
- **CI/CD & GitOps:** GitHub Actions, GitLab CI, ArgoCD, Jenkins
- **Monitoring & Observability:** Prometheus, Grafana, ELK Stack (Elasticsearch, Logstash, Kibana), OpenTelemetry
- **Scripting & OS:** Bash, Python, Linux (Debian, RedHat), Networking (TCP/IP, DNS, SSL/TLS, BGP)

---

### EXPERIENCE
**Senior DevOps Engineer** | CloudScale Technologies, Bengaluru  
*October 2022 – Present*
- Provisioned scalable multi-region AWS cloud infrastructure via modular Terraform templates, cutting environment setup time from 3 days to 25 minutes.
- Migrated 30+ monolithic services into containerized Kubernetes pods on AWS EKS, reducing overall cloud compute expenditure by ₹18 Lakhs annually.
- Integrated automated security vulnerability scanning with Trivy and SonarQube into CI/CD pipelines, eliminating 95% of critical CVEs prior to production.
- Architected comprehensive Prometheus/Grafana alerting dashboards, cutting Mean Time to Detect (MTTD) incidents by 45%.

**DevOps & Cloud Engineer** | InfraNxt Systems, Chennai  
*August 2020 – September 2022*
- Maintained 24/7 on-call rotational support for distributed payments infrastructure with 99.99% uptime compliance.
- Automated daily database backup snapshots, replication validation, and point-in-time recovery testing scripts.
- Implemented zero-downtime Blue-Green deployment pipelines with automated rollback triggers using ArgoCD.

---

### KEY PROJECTS
**Automated Kubernetes Multi-Cluster GitOps Platform** | *ArgoCD, Helm, EKS, Terraform*
- Built centralized GitOps repository deploying microservices automatically across staging and production clusters upon pull request approvals.
- Integrated automated certificate generation with cert-manager and Let's Encrypt.

**Enterprise Distributed Logging & Tracing Pipeline** | *Prometheus, Grafana, Loki, Tempo*
- Aggregated logs across 120+ microservices instances, providing real-time log querying and distributed latency tracing.

---

### EDUCATION & CERTIFICATIONS
**B.E. in Information Technology** | Anna University, Chennai  
- AWS Certified Solutions Architect – Associate
- Certified Kubernetes Administrator (CKA)
"""
    },

    "UI/UX & Product Designer (Human-Centered Design)": {
        "domain": "UI/UX Design",
        "desc": "Engineered for UI/UX Designers and Product Designers focusing on user research, design systems, and business outcomes.",
        "content": """# FIRSTNAME LASTNAME
Mumbai, India | +91 97654 32109 | designer@example.com | portfolio-link.com | linkedin.com/in/yourprofile

---

### PROFESSIONAL SUMMARY
Senior UI/UX Product Designer with 4+ years of experience transforming complex workflows into intuitive, elegant digital interfaces. Skilled in end-to-end human-centered design: qualitative user research, design system tokenization, and high-fidelity prototyping. Led product redesigns resulting in a 28% increase in task completion rates and 18% improvement in customer NPS.

---

### DESIGN EXPERTISE
- **Product Design:** Wireframing, User Journey Mapping, Information Architecture, Heuristic Evaluation, Interaction Design
- **Design Tools:** Figma (Auto Layout, Variables, Component Sets), FigJam, Miro, Adobe Creative Suite
- **User Research:** Semi-Structured Interviews, Usability Testing, Card Sorting, A/B Testing, Personas
- **Design Systems:** Design Tokens, Typography Scales, Accessibility (WCAG 2.1 AA), Component Governance
- **Collaboration & Handoff:** Dev Redlines, Zeplin, Jira, Agile Product Sprints, HTML/CSS Basics

---

### EXPERIENCE
**Lead Product Designer** | FinTech Innovations, Mumbai  
*May 2022 – Present*
- Led end-to-end UX research and interface design for a mobile investment app used by 400,000+ active investors in India.
- Conducted 30+ moderated user usability sessions, identifying critical onboarding hurdles and improving day-1 activation by 28%.
- Built and governed the company-wide Figma design system of 120+ modular components and semantic tokens, cutting frontend design turnaround by 35%.
- Facilitated quarterly design sprints and co-creation workshops with engineering, product, and compliance leaders.

**UI/UX Designer** | Creative Studio Digital, Bengaluru  
*July 2020 – April 2022*
- Redesigned enterprise healthcare portal, simplifying complex patient history workflows and elevating SUS score from 58 to 82.
- Created micro-interaction animations using Figma Smart Animate, providing engineering teams with clear interaction specs.

---

### PORTFOLIO CASE STUDIES
**Mobile Banking Digital Onboarding Redesign** | *Figma, User Testing, Auto Layout*
- Audited legacy multi-step KYC verification workflow and replaced it with a progressive disclosure step-wizard.
- Reduced average user signup drop-off rate from 42% to 17% in pilot testing.

**B2B SaaS Analytics Dashboard & Design System** | *Figma, Design Tokens, Miro*
- Designed responsive multi-tenant analytics dashboard featuring dark and light modes, customizable widget grids, and export flows.

---

### EDUCATION
**Bachelor of Design (B.Des) in Industrial / Communication Design**  
National Institute of Design (NID), India
"""
    },

    "Product Manager & Technical Program Lead": {
        "domain": "Product Management",
        "desc": "Curated for PMs, Product Owners, and Program Managers highlighting product vision, roadmaps, and commercial metrics.",
        "content": """# FIRSTNAME LASTNAME
Bengaluru, India | +91 98111 22334 | pm.lead@example.com | linkedin.com/in/yourprofile

---

### PROFESSIONAL SUMMARY
Data-informed Product Manager with 5+ years of experience leading cross-functional teams to build and scale B2B and consumer tech products. Proven ability to translate ambiguous customer problems into clear product roadmaps, data-backed PRDs, and measurable commercial growth. Spearheaded product initiatives resulting in ₹1.2 Cr in incremental ARR and a 32% boost in retention.

---

### CORE COMPETENCIES
- **Product Strategy:** Vision & Roadmapping, Problem Discovery, PRD Authoring, RICE Prioritization, Market Sizing
- **Data & Experimentation:** A/B Testing, Cohort Analysis, North Star Metric Alignment, SQL, Mixpanel, Google Analytics
- **Agile & Execution:** Scrum Leadership, Backlog Grooming, Jira, Sprint Planning, Release Management
- **Go-To-Market (GTM):** Customer Interviews, Competitive Benchmarking, Pricing & Packaging, Stakeholder Alignment

---

### WORK EXPERIENCE
**Senior Product Manager** | RapidScale B2B SaaS, Bengaluru  
*August 2022 – Present*
- Owned the core monetization and onboarding roadmap, driving an 18% improvement in trial-to-paid conversion in 6 months.
- Authored detailed PRDs and led a team of 10 software engineers and 2 product designers in bi-weekly agile sprint cadences.
- Re-architected team collaboration pricing tiers based on extensive customer willingness-to-pay interviews, yielding ₹85 Lakhs in annual expansion revenue.
- Defined North Star and input metrics, establishing live Mixpanel analytics dashboards for company executive reporting.

**Product Manager** | Consumer Commerce Hub, Gurugram  
*January 2020 – July 2022*
- Launched localized one-click checkout experience across Tier-2 and Tier-3 Indian cities, accelerating order volume by 25%.
- Formulated and executed 40+ iterative A/B tests across payment gateways, cart recommendations, and coupon UX.
- Partnered closely with customer support and legal teams to ensure strict RBI compliance and fraud prevention.

---

### PROVEN ACHIEVEMENTS & CASE STUDIES
**Enterprise API Self-Serve Developer Portal** | *Jira, Confluence, Mixpanel*
- Led zero-to-one launch of developer portal with interactive API documentation, lowering developer onboarding time from 14 days to 48 hours.
- Achieved a 4.8 / 5.0 developer satisfaction score in post-launch surveys.

---

### EDUCATION
**MBA in Technology Management / Marketing** | Premier B-School, India  
**B.Tech in Computer Science & Engineering** | Reputed University, India
"""
    }
}
