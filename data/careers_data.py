"""
Comprehensive dataset for 25 high-demand tech careers.
All salary metrics represent estimated current Indian market CTC packages (in INR Lakhs per Annum).
All learning paths, projects, and interview questions are structured for pure Python consumption.
"""

from pathlib import Path

BASE_ASSETS = Path(__file__).resolve().parent.parent / "assets"

CAREERS_DATA = {
    "Frontend Developer": {
        "icon": "💻",
        "category": "Web Development",
        "image": str(BASE_ASSETS / "front1.jpg"),
        "tagline": "Build beautiful, responsive, and high-performance user interfaces for modern web applications.",
        "salary_range": "₹4.5L – ₹15L LPA (Est. India Market)",
        "salary_details": [
            {"level": "Junior Frontend Dev (0–2 yrs)", "salary": "₹4L – ₹7L LPA", "exp": "0–2 years"},
            {"level": "Mid-Level Frontend Dev (2–4 yrs)", "salary": "₹7L – ₹13L LPA", "exp": "2–4 years"},
            {"level": "Senior Frontend Dev (4–7 yrs)", "salary": "₹13L – ₹22L LPA", "exp": "4–7 years"},
            {"level": "Staff / Frontend Architect (7+ yrs)", "salary": "₹22L – ₹35L+ LPA", "exp": "7+ years"}
        ],
        "demand": "High Demand",
        "est_time": "3–4 months",
        "readiness_base": 45,
        "readiness_max": 95,
        "skills": [
            {"name": "HTML5 & Semantic Markup", "current": 80, "required": 95},
            {"name": "CSS3, Flexbox & CSS Grid", "current": 75, "required": 90},
            {"name": "Modern JavaScript (ES6+)", "current": 60, "required": 90},
            {"name": "React.js / Next.js", "current": 40, "required": 85},
            {"name": "Tailwind CSS & Responsive UI", "current": 55, "required": 80},
            {"name": "TypeScript", "current": 30, "required": 75},
            {"name": "Web Performance & SEO", "current": 35, "required": 70}
        ],
        "phases": [
            {
                "num": "Phase 1",
                "name": "Web Foundations",
                "duration": "0 – 3 weeks",
                "tags": ["HTML5", "CSS3", "Flexbox", "CSS Grid", "Responsive Design", "Git & GitHub"]
            },
            {
                "num": "Phase 2",
                "name": "JavaScript Deep Dive",
                "duration": "3 – 6 weeks",
                "tags": ["ES6+ Syntax", "DOM Manipulation", "Async/Await", "Fetch API", "Event Loops", "NPM"]
            },
            {
                "num": "Phase 3",
                "name": "React Ecosystem",
                "duration": "6 – 10 weeks",
                "tags": ["React.js", "Hooks & State", "Tailwind CSS", "React Router", "Vite", "Component Architecture"]
            },
            {
                "num": "Phase 4",
                "name": "Production & Advanced",
                "duration": "10 – 16 weeks",
                "tags": ["TypeScript", "Next.js (App Router)", "State Management (Zustand/Redux)", "Vitest / Jest", "CI/CD Deployment"]
            }
        ],
        "resources": [
            {"name": "MDN Web Docs", "desc": "Standard reference for HTML, CSS, and JavaScript APIs", "type": "Documentation", "cost": "Free", "url": "https://developer.mozilla.org"},
            {"name": "javascript.info", "desc": "From beginner to advanced modern JavaScript tutorials", "type": "Tutorial", "cost": "Free", "url": "https://javascript.info"},
            {"name": "Official React Documentation", "desc": "Interactive, modern component guidelines", "type": "Documentation", "cost": "Free", "url": "https://react.dev"},
            {"name": "freeCodeCamp Responsive Web Design", "desc": "Hands-on projects and coding challenges", "type": "Course", "cost": "Free", "url": "https://www.freecodecamp.org"},
            {"name": "Frontend Masters", "desc": "In-depth masterclasses by industry practitioners", "type": "Video Platform", "cost": "Paid", "url": "https://frontendmasters.com"}
        ],
        "projects": [
            {"title": "Responsive Developer Portfolio", "difficulty": "Beginner", "tech": ["HTML5", "CSS3", "JavaScript"], "objectives": ["Fluid responsive layout", "Dark/Light mode toggle", "Contact form validation"]},
            {"title": "Real-time Weather Dashboard", "difficulty": "Beginner", "tech": ["JavaScript", "Fetch API", "Tailwind CSS"], "objectives": ["Geolocation integration", "7-day forecast cards", "Debounced search"]},
            {"title": "Interactive E-Commerce Product Catalog", "difficulty": "Intermediate", "tech": ["React", "Tailwind CSS", "Context API"], "objectives": ["Multi-attribute filtering", "Persistent cart storage", "Optimistic checkout UI"]},
            {"title": "SaaS Management & Analytics Dashboard", "difficulty": "Intermediate", "tech": ["Next.js", "TypeScript", "Recharts"], "objectives": ["Server-side rendering", "Dynamic chart visualization", "Role-based views"]},
            {"title": "Real-Time Collaborative Markdown Editor", "difficulty": "Advanced", "tech": ["Next.js", "WebSockets", "Tailwind"], "objectives": ["Live multi-user cursor sync", "Syntax highlighted preview", "Document export to PDF"]}
        ],
        "stages": [
            {"title": "Stage 1: Core Web Fundamentals", "duration": "2 weeks", "milestones": ["Master semantic HTML5 structure", "Implement responsive Flexbox & Grid layouts", "Build mobile-first navigation systems"]},
            {"title": "Stage 2: JavaScript Mastery & Async Programming", "duration": "4 weeks", "milestones": ["Master ES6+ closures, promises, and async/await", "Handle complex browser DOM events and bubbling", "Integrate external REST APIs with robust error handling"]},
            {"title": "Stage 3: Component-Driven Development with React", "duration": "5 weeks", "milestones": ["Build modular components with useState, useEffect, and custom hooks", "Implement client-side routing with React Router", "Style responsive interfaces with Tailwind CSS utility classes"]},
            {"title": "Stage 4: Production Architecture, TypeScript & Deployment", "duration": "5 weeks", "milestones": ["Refactor codebase to TypeScript with strict typings", "Implement Server-Side Rendering (SSR) in Next.js", "Set up automated tests and deploy to Vercel/Netlify"]}
        ],
        "interview": [
            {"category": "Technical", "q": "What is the Virtual DOM and how does React's reconciliation algorithm work?", "tip": "Explain how React computes differences (diffing algorithm) between the previous and new virtual DOM trees to minimize costly real DOM updates."},
            {"category": "Technical", "q": "Explain event bubbling and event capturing in JavaScript. How does event delegation leverage this?", "tip": "Detail the 3 phases: capturing, target, bubbling. Explain putting one listener on a parent element to handle dynamic child clicks efficiently."},
            {"category": "Case", "q": "How would you optimize the Core Web Vitals (LCP, FID/INP, CLS) of a slow, image-heavy web page?", "tip": "Cover image formats (WebP/AVIF), responsive picture tags, lazy loading below-the-fold content, font-display: swap, and code-splitting bundles."},
            {"category": "Behavioral", "q": "Describe a situation where a designer gave you a UI mockup that was technically infeasible or bad for web performance.", "tip": "Focus on collaborative communication, offering compromise alternatives that preserve design intent while keeping rendering efficient."}
        ]
    },

    "Backend Developer": {
        "icon": "⚙️",
        "category": "Web Development",
        "image": str(BASE_ASSETS / "backend1.png"),
        "tagline": "Architect resilient APIs, database schemas, and scalable server-side systems.",
        "salary_range": "₹5L – ₹18L LPA (Est. India Market)",
        "salary_details": [
            {"level": "Junior Backend Dev (0–2 yrs)", "salary": "₹5L – ₹8L LPA", "exp": "0–2 years"},
            {"level": "Mid-Level Backend Dev (2–4 yrs)", "salary": "₹8L – ₹15L LPA", "exp": "2–4 years"},
            {"level": "Senior Backend Dev (4–7 yrs)", "salary": "₹15L – ₹26L LPA", "exp": "4–7 years"},
            {"level": "Lead Architect (7+ yrs)", "salary": "₹26L – ₹40L+ LPA", "exp": "7+ years"}
        ],
        "demand": "Very High",
        "est_time": "4–6 months",
        "readiness_base": 40,
        "readiness_max": 92,
        "skills": [
            {"name": "Python (FastAPI/Django) / Node.js", "current": 55, "required": 90},
            {"name": "Relational Databases (PostgreSQL / MySQL)", "current": 50, "required": 85},
            {"name": "RESTful & GraphQL API Design", "current": 45, "required": 85},
            {"name": "Caching & Queues (Redis / RabbitMQ)", "current": 30, "required": 75},
            {"name": "Authentication & Security (OAuth2, JWT)", "current": 40, "required": 85},
            {"name": "System Design & Microservices", "current": 25, "required": 80}
        ],
        "phases": [
            {"num": "Phase 1", "name": "Server Foundations", "duration": "0 – 4 weeks", "tags": ["HTTP Protocols", "Python/Node.js", "REST Architecture", "CRUD Operations", "Git"]},
            {"num": "Phase 2", "name": "Databases & ORMs", "duration": "4 – 8 weeks", "tags": ["PostgreSQL", "SQL Schema Design", "Indexes & Query Plans", "Prisma / SQLAlchemy", "Transactions"]},
            {"num": "Phase 3", "name": "Auth, Caching & Scaling", "duration": "8 – 12 weeks", "tags": ["JWT & Sessions", "Bcrypt Hashing", "Redis Caching", "Rate Limiting", "Background Workers"]},
            {"num": "Phase 4", "name": "Microservices & Cloud Deploy", "duration": "12 – 18 weeks", "tags": ["Docker", "Message Brokers (Kafka/RabbitMQ)", "System Design", "AWS/GCP Setup", "Monitoring"]}
        ],
        "resources": [
            {"name": "FastAPI Official Documentation", "desc": "High-performance Python web framework documentation", "type": "Documentation", "cost": "Free", "url": "https://fastapi.tiangolo.com"},
            {"name": "PostgreSQL Tutorial", "desc": "Comprehensive SQL and schema design reference", "type": "Tutorial", "cost": "Free", "url": "https://www.postgresqltutorial.com"},
            {"name": "Designing Data-Intensive Applications", "desc": "Gold standard book on reliable, scalable systems", "type": "Book", "cost": "Paid", "url": "https://dataintensive.net"},
            {"name": "ByteByteGo System Design", "desc": "Visual system design guides and architectural patterns", "type": "Platform", "cost": "Free / Paid", "url": "https://bytebytego.com"}
        ],
        "projects": [
            {"title": "Secure Authentication & RBAC Service", "difficulty": "Beginner", "tech": ["Python", "FastAPI", "JWT", "Bcrypt"], "objectives": ["Token refresh rotation", "Role-based route guards", "Audit logs"]},
            {"title": "High-Throughput E-commerce Order API", "difficulty": "Intermediate", "tech": ["Node.js/Express", "PostgreSQL", "Redis"], "objectives": ["ACID inventory deduction", "Redis flash sale lock", "Pagination"]},
            {"title": "Real-time Chat & Notification Engine", "difficulty": "Intermediate", "tech": ["Python", "WebSockets", "Redis Pub/Sub"], "objectives": ["Room broadcast channels", "Offline message queue", "Typing indicators"]},
            {"title": "Distributed Task Queue & Video Processor", "difficulty": "Advanced", "tech": ["FastAPI", "Celery / RabbitMQ", "S3"], "objectives": ["Asynchronous video transcoding", "Status webhooks", "Retry backoffs"]}
        ],
        "stages": [
            {"title": "Stage 1: Server Logic & REST Architecture", "duration": "3 weeks", "milestones": ["Understand HTTP methods, status codes, and headers", "Build structured REST endpoints with input validation", "Handle global error exceptions and logging"]},
            {"title": "Stage 2: Database Modeling & Performance", "duration": "4 weeks", "milestones": ["Design normalized relational database schemas", "Write complex joins, aggregations, and subqueries", "Analyze EXPLAIN query plans and build effective B-Tree indexes"]},
            {"title": "Stage 3: Security, Auth & Caching", "duration": "4 weeks", "milestones": ["Implement secure JWT authentication with refresh rotation", "Mitigate OWASP Top 10 vulnerabilities (SQLi, XSS, CSRF)", "Integrate Redis caching for hot database queries"]},
            {"title": "Stage 4: Scalable Architecture & Containerization", "duration": "5 weeks", "milestones": ["Containerize backend applications using Docker & multi-stage builds", "Design asynchronous message workflows using RabbitMQ/Kafka", "Implement health checks, metrics, and Prometheus monitoring"]}
        ],
        "interview": [
            {"category": "Technical", "q": "What is the difference between SQL and NoSQL databases, and when would you choose which?", "tip": "Contrast ACID compliance, relational integrity, and schema rigidity with horizontal partitioning, dynamic schemas, and document/key-value access."},
            {"category": "Technical", "q": "How do database indexes work, and what are the trade-offs of adding too many indexes?", "tip": "Explain B-Tree balanced structures enabling logarithmic lookups, but highlight write performance penalties on INSERT/UPDATE/DELETE operations."},
            {"category": "Case", "q": "How would you design a URL shortener service (like Bitly) to handle 100 million writes per day?", "tip": "Discuss Base62 encoding, hash collision strategies, distributed key generation service (KGS), Redis read caching, and read-heavy replication."}
        ]
    },

    "Full Stack Developer": {
        "icon": "🌐",
        "category": "Web Development",
        "image": str(BASE_ASSETS / "ful.png"),
        "tagline": "Master the entire stack: user-facing interfaces, APIs, databases, and deployment.",
        "salary_range": "₹6L – ₹20L LPA (Est. India Market)",
        "salary_details": [
            {"level": "Junior Full Stack Dev", "salary": "₹6L – ₹9L LPA", "exp": "0–2 years"},
            {"level": "Mid-Level Full Stack Dev", "salary": "₹9L – ₹17L LPA", "exp": "2–4 years"},
            {"level": "Senior Full Stack Dev", "salary": "₹17L – ₹28L LPA", "exp": "4–7 years"},
            {"level": "Lead Full Stack Architect", "salary": "₹28L – ₹45L+ LPA", "exp": "7+ years"}
        ],
        "demand": "Top Demand",
        "est_time": "6–8 months",
        "readiness_base": 35,
        "readiness_max": 90,
        "skills": [
            {"name": "Frontend (React / Next.js)", "current": 55, "required": 85},
            {"name": "Backend (Node.js / Python)", "current": 50, "required": 85},
            {"name": "Databases (SQL & NoSQL)", "current": 45, "required": 80},
            {"name": "API Integration & State Management", "current": 50, "required": 85},
            {"name": "DevOps & Cloud Deployment", "current": 30, "required": 75}
        ],
        "phases": [
            {"num": "Phase 1", "name": "Frontend Excellence", "duration": "0 – 6 weeks", "tags": ["HTML/CSS/JS", "React.js", "Tailwind CSS", "Client State"]},
            {"num": "Phase 2", "name": "Backend & Database", "duration": "6 – 12 weeks", "tags": ["Node/Express or Python", "PostgreSQL", "REST APIs", "Prisma"]},
            {"num": "Phase 3", "name": "Full Stack Integration", "duration": "12 – 18 weeks", "tags": ["Next.js Full Stack", "Server Actions", "Auth.js", "Payment Gateways (Stripe/Razorpay)"]},
            {"num": "Phase 4", "name": "Production & DevOps", "duration": "18 – 24 weeks", "tags": ["Docker", "CI/CD Actions", "Cloud Hosting (AWS/Vercel)", "Telemetry"]}
        ],
        "resources": [
            {"name": "Full Stack Open (University of Helsinki)", "desc": "World-class hands-on modern full-stack web course", "type": "Course", "cost": "Free", "url": "https://fullstackopen.com/en/"},
            {"name": "Next.js Learn Course", "desc": "Official interactive full-stack Next.js guide", "type": "Course", "cost": "Free", "url": "https://nextjs.org/learn"},
            {"name": "The Odin Project", "desc": "Curated full-stack curriculum with portfolio projects", "type": "Curriculum", "cost": "Free", "url": "https://www.theodinproject.com"}
        ],
        "projects": [
            {"title": "Multi-Tenant SaaS Starter Boilerplate", "difficulty": "Advanced", "tech": ["Next.js", "PostgreSQL", "Tailwind", "Stripe"], "objectives": ["Organization workspaces", "Subscription billing tiers", "Admin telemetry"]},
            {"title": "Collaborative Task & Sprint Board", "difficulty": "Intermediate", "tech": ["React", "FastAPI", "PostgreSQL", "WebSockets"], "objectives": ["Drag and drop Kanban", "Instant updates across users", "Activity log"]}
        ],
        "stages": [
            {"title": "Stage 1: Frontend Interface Mastery", "duration": "6 weeks", "milestones": ["Build modern responsive UIs with React", "Manage asynchronous server state", "Integrate client routing"]},
            {"title": "Stage 2: Backend Services & Storage", "duration": "6 weeks", "milestones": ["Build secure authenticated backend endpoints", "Model normalized databases and migrations", "Implement input sanitization"]},
            {"title": "Stage 3: Full Stack Systems Integration", "duration": "6 weeks", "milestones": ["Create unified full-stack applications with Next.js", "Integrate payment processing and webhooks", "Implement email delivery services"]},
            {"title": "Stage 4: Automated Testing & Deployment", "duration": "4 weeks", "milestones": ["Write unit and end-to-end integration tests", "Configure automated CI/CD pipeline", "Deploy to production cloud infrastructure"]}
        ],
        "interview": [
            {"category": "Technical", "q": "Compare Client-Side Rendering (CSR), Server-Side Rendering (SSR), and Static Site Generation (SSG).", "tip": "Break down TTFB (Time to First Byte), FCP (First Contentful Paint), SEO crawlability, and server compute costs for each strategy."},
            {"category": "Technical", "q": "How do you securely handle user sessions and authentication in a decoupled SPA + API architecture?", "tip": "Explain HttpOnly, Secure, SameSite cookies vs localStorage, and talk about CSRF protection and access/refresh token lifecycles."}
        ]
    },

    "Data Scientist": {
        "icon": "📊",
        "category": "Data Science & Analytics",
        "image": str(BASE_ASSETS / "data1.png"),
        "tagline": "Transform complex datasets into actionable predictive insights and AI business models.",
        "salary_range": "₹6L – ₹25L LPA (Est. India Market)",
        "salary_details": [
            {"level": "Junior Data Scientist", "salary": "₹6L – ₹10L LPA", "exp": "0–2 years"},
            {"level": "Mid-Level Data Scientist", "salary": "₹10L – ₹18L LPA", "exp": "2–5 years"},
            {"level": "Senior Data Scientist", "salary": "₹18L – ₹30L LPA", "exp": "5–8 years"},
            {"level": "Principal Data Scientist", "salary": "₹30L – ₹50L+ LPA", "exp": "8+ years"}
        ],
        "demand": "Trending",
        "est_time": "5–7 months",
        "readiness_base": 30,
        "readiness_max": 90,
        "skills": [
            {"name": "Python & Data Libraries (Pandas, NumPy)", "current": 65, "required": 95},
            {"name": "Probability & Applied Statistics", "current": 45, "required": 85},
            {"name": "Machine Learning (Scikit-Learn)", "current": 40, "required": 85},
            {"name": "Data Visualization (Seaborn, Plotly)", "current": 50, "required": 80},
            {"name": "SQL & Relational Analytics", "current": 55, "required": 90},
            {"name": "Deep Learning & NLP Basics", "current": 25, "required": 75}
        ],
        "phases": [
            {"num": "Phase 1", "name": "Python & Math Foundations", "duration": "0 – 4 weeks", "tags": ["Python", "Pandas", "NumPy", "Linear Algebra", "Calculus", "Descriptive Stats"]},
            {"num": "Phase 2", "name": "EDA & Inferential Statistics", "duration": "4 – 8 weeks", "tags": ["Hypothesis Testing", "A/B Testing", "Seaborn", "Feature Engineering", "SQL Analytics"]},
            {"num": "Phase 3", "name": "Supervised & Unsupervised ML", "duration": "8 – 14 weeks", "tags": ["Scikit-Learn", "Regression", "Tree Ensembles (XGBoost)", "Clustering", "Cross-Validation"]},
            {"num": "Phase 4", "name": "Model Deployment & Advanced ML", "duration": "14 – 20 weeks", "tags": ["FastAPI Model Serving", "Streamlit Apps", "MLflow Tracking", "Deep Learning Fundamentals"]}
        ],
        "resources": [
            {"name": "Kaggle Learn & Competitions", "desc": "Practical micro-courses and real-world datasets", "type": "Platform", "cost": "Free", "url": "https://www.kaggle.com"},
            {"name": "StatQuest with Josh Starmer", "desc": "Visual step-by-step statistics and ML concepts", "type": "YouTube Channel", "cost": "Free", "url": "https://statquest.org"},
            {"name": "Coursera Machine Learning Specialization", "desc": "Andrew Ng's world-renowned ML foundation series", "type": "Course", "cost": "Free / Paid", "url": "https://www.coursera.org"}
        ],
        "projects": [
            {"title": "Customer Churn Prediction Engine", "difficulty": "Intermediate", "tech": ["Python", "Pandas", "XGBoost", "Streamlit"], "objectives": ["Data imputation & scaling", "Feature importance breakdown", "Interactive risk calculator"]},
            {"title": "Healthcare Diagnostic Risk Classifier", "difficulty": "Intermediate", "tech": ["Scikit-learn", "ROC-AUC", "FastAPI"], "objectives": ["Class imbalance handling (SMOTE)", "Precision-recall tuning", "Inference API"]}
        ],
        "stages": [
            {"title": "Stage 1: Scientific Python & Matrix Computation", "duration": "4 weeks", "milestones": ["Master NumPy vectorization and memory layouts", "Wrangle messy real-world datasets with Pandas", "Perform exploratory data visualization"]},
            {"title": "Stage 2: Statistical Modeling & Inference", "duration": "4 weeks", "milestones": ["Formulate null/alternative hypotheses and p-values", "Conduct rigorous A/B test experiments", "Clean outliers and handle multicollinearity"]},
            {"title": "Stage 3: Applied Machine Learning Algorithms", "duration": "6 weeks", "milestones": ["Train linear, ridge, lasso, and logistic regressions", "Tune Random Forests and XGBoost gradient boosters", "Evaluate with Precision, Recall, F1, and ROC-AUC curves"]},
            {"title": "Stage 4: Model Serving & Portfolio Deployment", "duration": "4 weeks", "milestones": ["Serialize models using joblib / ONNX", "Build inference microservices with FastAPI", "Deploy interactive machine learning dashboards"]}
        ],
        "interview": [
            {"category": "Technical", "q": "What is the Bias-Variance tradeoff, and how do ensemble methods like Random Forest and Gradient Boosting address it?", "tip": "Explain underfitting vs overfitting. Random Forest reduces variance via bagging; Boosting reduces bias via sequential gradient fitting."},
            {"category": "Case", "q": "You train a credit card fraud detection model that achieves 99.2% accuracy. Why is this metric dangerous, and what would you use instead?", "tip": "Point out extreme class imbalance. 99% accuracy can just predict 'non-fraud' always. Recommend Precision, Recall, PR-AUC, and Cost-Weighted loss."}
        ]
    },

    "AI Engineer": {
        "icon": "🤖",
        "category": "AI & Machine Learning",
        "image": str(BASE_ASSETS / "ai.png"),
        "tagline": "Build intelligent agents, Generative AI applications, and Large Language Model architectures.",
        "salary_range": "₹8L – ₹35L LPA (Est. India Market)",
        "salary_details": [
            {"level": "Junior AI Engineer", "salary": "₹8L – ₹14L LPA", "exp": "0–2 years"},
            {"level": "Mid-Level AI Engineer", "salary": "₹14L – ₹24L LPA", "exp": "2–5 years"},
            {"level": "Senior AI Engineer", "salary": "₹24L – ₹38L LPA", "exp": "5–8 years"},
            {"level": "Lead AI Scientist / Architect", "salary": "₹38L – ₹60L+ LPA", "exp": "8+ years"}
        ],
        "demand": "Trending",
        "est_time": "6–9 months",
        "readiness_base": 25,
        "readiness_max": 85,
        "skills": [
            {"name": "Python & PyTorch", "current": 40, "required": 90},
            {"name": "LLM APIs & Prompt Engineering", "current": 60, "required": 95},
            {"name": "RAG & Vector Databases (Chroma/Pinecone)", "current": 35, "required": 90},
            {"name": "LangChain & LlamaIndex", "current": 35, "required": 85},
            {"name": "Fine-Tuning & Model Evaluation", "current": 20, "required": 75},
            {"name": "AI Agent Systems & Tools", "current": 25, "required": 80}
        ],
        "phases": [
            {"num": "Phase 1", "name": "AI Foundations & Deep Learning", "duration": "0 – 6 weeks", "tags": ["Neural Networks", "PyTorch", "Backpropagation", "Tensors", "Transformers Architecture"]},
            {"num": "Phase 2", "name": "LLMs & Retrieval-Augmented Generation", "duration": "6 – 12 weeks", "tags": ["Embeddings", "Vector DBs", "Chunking Strategies", "Semantic Search", "RAG Pipelines"]},
            {"num": "Phase 3", "name": "Agentic Workflows & Multi-Agent Teams", "duration": "12 – 18 weeks", "tags": ["LangGraph", "Tool Calling", "Autonomous Agents", "Evaluation Frameworks (Ragas)"]},
            {"num": "Phase 4", "name": "Fine-Tuning, Quantization & MLOps", "duration": "18 – 24 weeks", "tags": ["LoRA / QLoRA", "Hugging Face", "vLLM Inference", "Model Monitoring", "Cloud GPU Serving"]}
        ],
        "resources": [
            {"name": "DeepLearning.AI Short Courses", "desc": "Pioneering LLM, LangChain, and RAG courses by Andrew Ng", "type": "Course", "cost": "Free", "url": "https://www.deeplearning.ai"},
            {"name": "Hugging Face NLP Course", "desc": "Practical transformer training and fine-tuning reference", "type": "Documentation", "cost": "Free", "url": "https://huggingface.co/learn/nlp-course"},
            {"name": "Fast.ai Practical Deep Learning", "desc": "Top-down practitioner-first deep learning curriculum", "type": "Course", "cost": "Free", "url": "https://www.fast.ai"}
        ],
        "projects": [
            {"title": "Enterprise RAG Document Q&A Assistant", "difficulty": "Intermediate", "tech": ["Python", "LangChain", "ChromaDB", "Streamlit"], "objectives": ["Hierarchical document chunking", "Hybrid BM25 + dense retrieval", "Source citation rendering"]},
            {"title": "Autonomous Multi-Agent Code Auditor", "difficulty": "Advanced", "tech": ["LangGraph", "Python", "Tool Calling"], "objectives": ["Static security analysis agent", "Automated patch proposal", "Human-in-the-loop review"]}
        ],
        "stages": [
            {"title": "Stage 1: Deep Learning Fundamentals", "duration": "5 weeks", "milestones": ["Understand neural architectures, activations, and backpropagation", "Build feedforward and convolutional models in PyTorch", "Understand Transformer self-attention mechanisms"]},
            {"title": "Stage 2: LLM Pipelines & RAG Systems", "duration": "5 weeks", "milestones": ["Generate text embeddings and store vectors in Pinecone/Chroma", "Design contextual chunking and re-ranking algorithms", "Evaluate retrieval quality and hallucination rates"]},
            {"title": "Stage 3: Agentic Systems & Function Calling", "duration": "5 weeks", "milestones": ["Implement tool use and structured JSON outputs", "Build stateful multi-step agent loops using LangGraph", "Add human confirmation breakpoints for safety"]},
            {"title": "Stage 4: Optimization & Production Serving", "duration": "5 weeks", "milestones": ["Fine-tune open-weights models with LoRA/PEFT", "Deploy models with fast inference engines (vLLM / Ollama)", "Implement guardrails and rate limiting"]}
        ],
        "interview": [
            {"category": "Technical", "q": "What is the difference between Fine-Tuning and RAG (Retrieval-Augmented Generation)? When do you choose each?", "tip": "RAG provides real-time, external, dynamic domain facts without retraining. Fine-tuning teaches style, format, tone, or specific proprietary task behavior."},
            {"category": "Technical", "q": "How does self-attention in the Transformer architecture work mathematically?", "tip": "Explain Query, Key, Value matrices, scaled dot-product attention formula: Softmax((QK^T)/sqrt(d_k))V, and multi-head representation."}
        ]
    },

    "Machine Learning Engineer": {
        "icon": "🧠",
        "category": "AI & Machine Learning",
        "image": str(BASE_ASSETS / "ma1.png"),
        "tagline": "Design, productionize, and scale predictive models on high-volume cloud infrastructure.",
        "salary_range": "₹8L – ₹30L LPA (Est. India Market)",
        "salary_details": [
            {"level": "Junior ML Engineer", "salary": "₹8L – ₹13L LPA", "exp": "0–2 years"},
            {"level": "Mid-Level ML Engineer", "salary": "₹13L – ₹22L LPA", "exp": "2–5 years"},
            {"level": "Senior ML Engineer", "salary": "₹22L – ₹35L LPA", "exp": "5–8 years"},
            {"level": "Staff MLOps Architect", "salary": "₹35L – ₹55L+ LPA", "exp": "8+ years"}
        ],
        "demand": "High Demand",
        "est_time": "6–10 months",
        "readiness_base": 25,
        "readiness_max": 88,
        "skills": [
            {"name": "ML Algorithms & Math", "current": 40, "required": 85},
            {"name": "PyTorch / TensorFlow", "current": 35, "required": 85},
            {"name": "MLOps & CI/CD for Models (MLflow)", "current": 20, "required": 90},
            {"name": "Model Serving & Docker APIs", "current": 30, "required": 85},
            {"name": "Feature Stores & Pipelines", "current": 25, "required": 80}
        ],
        "phases": [
            {"num": "Phase 1", "name": "Foundations", "duration": "0 – 6 weeks", "tags": ["Linear Algebra", "Python", "Scikit-Learn", "Model Evaluation"]},
            {"num": "Phase 2", "name": "Deep Learning Models", "duration": "6 – 12 weeks", "tags": ["PyTorch", "CNNs", "RNNs/Transformers", "GPU Acceleration"]},
            {"num": "Phase 3", "name": "MLOps & Pipelines", "duration": "12 – 18 weeks", "tags": ["MLflow", "DVC", "Airflow Pipelines", "Docker", "FastAPI"]},
            {"num": "Phase 4", "name": "Production & Monitoring", "duration": "18 – 24 weeks", "tags": ["Triton Server", "Data Drift Detection", "Kubernetes", "Prometheus"]}
        ],
        "resources": [
            {"name": "Made With ML by Goku Mohandas", "desc": "End-to-end MLOps from design to deployment", "type": "Curriculum", "cost": "Free", "url": "https://madewithml.com"},
            {"name": "Full Stack Deep Learning", "desc": "Course on production engineering for machine learning", "type": "Course", "cost": "Free", "url": "https://fullstackdeeplearning.com"}
        ],
        "projects": [
            {"title": "Real-time Fraud Scoring Pipeline", "difficulty": "Advanced", "tech": ["PyTorch", "FastAPI", "Docker", "Redis"], "objectives": ["Sub-50ms inference", "Feature caching", "Model versioning"]},
            {"title": "Automated ML Retraining Pipeline", "difficulty": "Advanced", "tech": ["MLflow", "Airflow", "DVC", "GitHub Actions"], "objectives": ["Data drift trigger", "Automated validation", "Registry promote"]}
        ],
        "stages": [
            {"title": "Stage 1: Production Code & Algorithm Foundations", "duration": "6 weeks", "milestones": ["Write clean, vectorized, tested Python code", "Implement core ML algorithms from scratch", "Set up experiment tracking"]},
            {"title": "Stage 2: Deep Learning Architectures", "duration": "6 weeks", "milestones": ["Train CNNs and Transformers in PyTorch", "Implement learning rate schedulers and mixed precision", "Export models to ONNX"]},
            {"title": "Stage 3: MLOps & Experiment Registries", "duration": "6 weeks", "milestones": ["Version data and models using DVC and MLflow", "Build automated training DAGs with Airflow", "Package models in reproducible Docker containers"]},
            {"title": "Stage 4: Low-Latency Inference & Drift Detection", "duration": "6 weeks", "milestones": ["Serve models with sub-100ms response SLAs", "Monitor feature distribution drift in production", "Implement zero-downtime canary model updates"]}
        ],
        "interview": [
            {"category": "Technical", "q": "What is data drift and concept drift, and how do you detect and remediate them in production?", "tip": "Data drift is P(X) changing (input distribution). Concept drift is P(Y|X) changing (relationship). Detect using KS-tests or PSI, remediate by triggering retraining pipelines."},
            {"category": "Technical", "q": "How would you optimize an ML model for low-latency, real-time inference on edge or cloud servers?", "tip": "Quantization (INT8), pruning weights, operator fusion, ONNX Runtime, and TensorRT engines."}
        ]
    },

    "Data Analyst": {
        "icon": "📈",
        "category": "Data Science & Analytics",
        "image": str(BASE_ASSETS / "dataanalyst.png"),
        "tagline": "Extract, analyze, and visualize data trends to guide critical commercial decisions.",
        "salary_range": "₹4L – ₹12L LPA (Est. India Market)",
        "salary_details": [
            {"level": "Junior Analyst (0–2 yrs)", "salary": "₹4L – ₹6.5L LPA", "exp": "0–2 years"},
            {"level": "Mid-Level Data Analyst (2–4 yrs)", "salary": "₹6.5L – ₹11L LPA", "exp": "2–4 years"},
            {"level": "Senior Analyst / BI Lead (4+ yrs)", "salary": "₹11L – ₹18L+ LPA", "exp": "4+ years"}
        ],
        "demand": "Growing",
        "est_time": "3–5 months",
        "readiness_base": 50,
        "readiness_max": 92,
        "skills": [
            {"name": "Advanced SQL & Database Queries", "current": 60, "required": 95},
            {"name": "Power BI / Tableau Visualizations", "current": 50, "required": 90},
            {"name": "Excel (Power Query, Pivot Tables)", "current": 70, "required": 90},
            {"name": "Python for Analytics (Pandas)", "current": 40, "required": 80},
            {"name": "Business Acumen & Storytelling", "current": 50, "required": 85}
        ],
        "phases": [
            {"num": "Phase 1", "name": "Excel & Business Foundations", "duration": "0 – 3 weeks", "tags": ["Excel Advanced", "Pivot Tables", "Power Query", "KPI Metrics"]},
            {"num": "Phase 2", "name": "SQL & Data Extraction", "duration": "3 – 7 weeks", "tags": ["Complex Joins", "Window Functions", "CTEs", "Subqueries", "Aggregations"]},
            {"num": "Phase 3", "name": "BI Dashboards & Visualization", "duration": "7 – 11 weeks", "tags": ["Power BI", "DAX Formulas", "Tableau", "Interactive Filters", "Storytelling"]},
            {"num": "Phase 4", "name": "Python & Automated Reporting", "duration": "11 – 15 weeks", "tags": ["Pandas", "Matplotlib/Seaborn", "Automated PDF Exports", "Stakeholder Reviews"]}
        ],
        "resources": [
            {"name": "SQLZoo Interactive SQL Tutorial", "desc": "Step-by-step SQL practice exercises", "type": "Practice", "cost": "Free", "url": "https://sqlzoo.net"},
            {"name": "Maven Analytics Learning Center", "desc": "Specialized courses in Excel, SQL, and Power BI", "type": "Platform", "cost": "Paid", "url": "https://www.mavenanalytics.io"}
        ],
        "projects": [
            {"title": "Retail Sales Performance & Retention Dashboard", "difficulty": "Intermediate", "tech": ["Power BI", "DAX", "SQL"], "objectives": ["YoY growth calculation", "Cohort retention analysis", "Dynamic drill-downs"]},
            {"title": "Customer Segmentation & RFM Analysis", "difficulty": "Intermediate", "tech": ["Python", "Pandas", "Seaborn"], "objectives": ["Recency/Frequency/Monetary scores", "Cluster visualization", "Actionable marketing deck"]}
        ],
        "stages": [
            {"title": "Stage 1: Advanced Spreadsheet Modeling", "duration": "3 weeks", "milestones": ["Master INDEX/MATCH, XLOOKUP, and dynamic arrays", "Automate data consolidation with Power Query", "Build executive summary scorecards"]},
            {"title": "Stage 2: Enterprise SQL Analytics", "duration": "4 weeks", "milestones": ["Write multi-table relational joins and subqueries", "Apply window functions (RANK, DENSE_RANK, LAG, LEAD)", "Optimize analytical queries with Common Table Expressions (CTEs)"]},
            {"title": "Stage 3: Interactive Business Intelligence Dashboards", "duration": "4 weeks", "milestones": ["Build star schema data models in Power BI", "Formulate complex DAX measures and calculated columns", "Design user-friendly KPI dashboards"]},
            {"title": "Stage 4: Python Analytics & Executive Storytelling", "duration": "4 weeks", "milestones": ["Clean messy CSV/JSON datasets with Pandas", "Identify seasonality and statistical correlations", "Present insights with actionable business recommendations"]}
        ],
        "interview": [
            {"category": "Technical", "q": "What is the difference between RANK, DENSE_RANK, and ROW_NUMBER in SQL?", "tip": "Give an example with identical values: ROW_NUMBER increments sequentially, RANK leaves gaps after ties, DENSE_RANK assigns consecutive numbers with no gaps."},
            {"category": "Case", "q": "A key business metric (Daily Active Users) drops 8% week-over-week. How do you triage and diagnose this drop?", "tip": "Break down systematically: data pipeline integrity, geography/platform splits, recent releases, external holidays, marketing channel shifts."}
        ]
    },

    "Cloud Engineer": {
        "icon": "☁️",
        "category": "Cloud & DevOps",
        "image": str(BASE_ASSETS / "cloud.png"),
        "tagline": "Design, deploy, and operate secure, cost-optimized cloud architectures on AWS/Azure/GCP.",
        "salary_range": "₹8L – ₹28L LPA (Est. India Market)",
        "salary_details": [
            {"level": "Junior Cloud Engineer", "salary": "₹8L – ₹12L LPA", "exp": "0–2 years"},
            {"level": "Mid-Level Cloud Engineer", "salary": "₹12L – ₹20L LPA", "exp": "2–5 years"},
            {"level": "Senior Cloud Architect", "salary": "₹20L – ₹35L+ LPA", "exp": "5+ years"}
        ],
        "demand": "Top Demand",
        "est_time": "5–8 months",
        "readiness_base": 30,
        "readiness_max": 90,
        "skills": [
            {"name": "AWS / Azure Services (IAM, VPC, EC2, S3)", "current": 45, "required": 95},
            {"name": "Infrastructure as Code (Terraform)", "current": 30, "required": 85},
            {"name": "Linux Administration & Shell Scripting", "current": 55, "required": 90},
            {"name": "Networking & Security (DNS, SSL, Firewalls)", "current": 40, "required": 85},
            {"name": "Containers & Serverless (ECS, Lambda)", "current": 35, "required": 80}
        ],
        "phases": [
            {"num": "Phase 1", "name": "Linux & Networking Fundamentals", "duration": "0 – 4 weeks", "tags": ["Linux CLI", "Bash", "TCP/IP", "DNS", "Subnets", "SSH"]},
            {"num": "Phase 2", "name": "Core Cloud Provider (AWS)", "duration": "4 – 10 weeks", "tags": ["IAM", "VPC", "EC2 AutoScaling", "S3 Storage", "RDS", "ALB"]},
            {"num": "Phase 3", "name": "Infrastructure as Code & Automation", "duration": "10 – 16 weeks", "tags": ["Terraform Modules", "CloudFormation", "Ansible", "GitOps"]},
            {"num": "Phase 4", "name": "Cloud Security, Serverless & Cost", "duration": "16 – 22 weeks", "tags": ["Lambda", "API Gateway", "WAF", "FinOps", "Disaster Recovery"]}
        ],
        "resources": [
            {"name": "AWS Skill Builder", "desc": "Official digital training pathways from Amazon Web Services", "type": "Platform", "cost": "Free / Paid", "url": "https://explore.skillbuilder.aws"},
            {"name": "Learn Terraform by HashiCorp", "desc": "Step-by-step guides for infrastructure as code", "type": "Tutorial", "cost": "Free", "url": "https://developer.hashicorp.com/terraform/tutorials"}
        ],
        "projects": [
            {"title": "Multi-Tier High Availability VPC Architecture", "difficulty": "Intermediate", "tech": ["Terraform", "AWS VPC", "EC2", "ALB", "RDS"], "objectives": ["Public/Private subnets", "Auto-scaling groups across 2 AZs", "NAT Gateways"]},
            {"title": "Serverless Event-Driven Image Pipeline", "difficulty": "Intermediate", "tech": ["AWS S3", "Lambda", "SQS", "DynamoDB"], "objectives": ["S3 event trigger", "Thumbnail creation", "Metadata persistence"]}
        ],
        "stages": [
            {"title": "Stage 1: Linux & Virtual Networking", "duration": "4 weeks", "milestones": ["Master Linux system permissions, processes, and network commands", "Configure CIDR blocks, route tables, and subnet masks", "Establish secure SSH bastion key authentication"]},
            {"title": "Stage 2: Core AWS Infrastructure", "duration": "6 weeks", "milestones": ["Enforce least-privilege IAM security policies and roles", "Deploy fault-tolerant EC2 instances behind Application Load Balancers", "Configure automated RDS backups and read replicas"]},
            {"title": "Stage 3: Infrastructure as Code with Terraform", "duration": "5 weeks", "milestones": ["Write reusable, modular Terraform configuration templates", "Manage remote state locking with S3 and DynamoDB", "Automate infrastructure validation in CI/CD pipelines"]},
            {"title": "Stage 4: Serverless, Cost & Security Optimization", "duration": "5 weeks", "milestones": ["Build event-driven microservices with AWS Lambda", "Configure CloudWatch metrics, alarms, and AWS Cost Explorer budgets", "Conduct disaster recovery failover simulations"]}
        ],
        "interview": [
            {"category": "Technical", "q": "Explain the 5 Pillars of the AWS Well-Architected Framework.", "tip": "Operational Excellence, Security, Reliability, Performance Efficiency, and Cost Optimization. Provide concrete examples for each."},
            {"category": "Technical", "q": "What is the difference between an IAM Role, IAM User, and IAM Policy?", "tip": "User has long-term credentials for a human. Policy is a JSON permission definition. Role is an assumable identity with short-term STS credentials."}
        ]
    },

    "DevOps Engineer": {
        "icon": "♾️",
        "category": "Cloud & DevOps",
        "image": str(BASE_ASSETS / "devops.png"),
        "tagline": "Automate continuous integration, container orchestration, and reliable delivery pipelines.",
        "salary_range": "₹8L – ₹30L LPA (Est. India Market)",
        "salary_details": [
            {"level": "Junior DevOps Engineer", "salary": "₹8L – ₹13L LPA", "exp": "0–2 years"},
            {"level": "Mid-Level DevOps Engineer", "salary": "₹13L – ₹22L LPA", "exp": "2–5 years"},
            {"level": "Senior DevOps / SRE Lead", "salary": "₹22L – ₹38L+ LPA", "exp": "5+ years"}
        ],
        "demand": "Top Demand",
        "est_time": "5–7 months",
        "readiness_base": 35,
        "readiness_max": 90,
        "skills": [
            {"name": "Linux & Bash Automation", "current": 60, "required": 95},
            {"name": "Docker & Containerization", "current": 45, "required": 90},
            {"name": "Kubernetes Orchestration", "current": 25, "required": 85},
            {"name": "CI/CD Pipelines (GitHub Actions/Jenkins)", "current": 40, "required": 90},
            {"name": "Infrastructure as Code (Terraform/Ansible)", "current": 30, "required": 85},
            {"name": "Monitoring & Telemetry (Prometheus/Grafana)", "current": 25, "required": 80}
        ],
        "phases": [
            {"num": "Phase 1", "name": "Linux & Scripting", "duration": "0 – 4 weeks", "tags": ["Linux Internals", "Shell Scripting", "Git Workflows", "Networking"]},
            {"num": "Phase 2", "name": "Containers & CI/CD", "duration": "4 – 9 weeks", "tags": ["Docker", "Multi-stage Builds", "GitHub Actions", "Automated Testing"]},
            {"num": "Phase 3", "name": "Kubernetes & Orchestration", "duration": "9 – 15 weeks", "tags": ["Pods", "Deployments", "Services", "Ingress", "Helm Charts"]},
            {"num": "Phase 4", "name": "GitOps, IaC & Observability", "duration": "15 – 22 weeks", "tags": ["Terraform", "ArgoCD", "Prometheus", "Grafana", "Loki"]}
        ],
        "resources": [
            {"name": "Kubernetes Official Documentation & Interactive Tutorials", "desc": "Reference guides and minikube sandboxes", "type": "Documentation", "cost": "Free", "url": "https://kubernetes.io/docs/home/"},
            {"name": "DevOps Roadmap by Roadmap.sh", "desc": "Community-driven visual learning milestones", "type": "Guide", "cost": "Free", "url": "https://roadmap.sh/devops"}
        ],
        "projects": [
            {"title": "End-to-End GitOps CI/CD Pipeline", "difficulty": "Advanced", "tech": ["GitHub Actions", "Docker", "Kubernetes", "ArgoCD"], "objectives": ["Automated test execution", "Container vulnerability scanning (Trivy)", "Canary rollout"]},
            {"title": "Cluster Monitoring Stack", "difficulty": "Intermediate", "tech": ["Prometheus", "Grafana", "Alertmanager"], "objectives": ["Cluster node CPU/Memory alerts", "Slack notification webhook", "Dashboard visualization"]}
        ],
        "stages": [
            {"title": "Stage 1: System Automation & Shell Scripting", "duration": "4 weeks", "milestones": ["Write modular bash automation scripts", "Configure secure SSH keys and user access", "Manage Linux systemd services and logs"]},
            {"title": "Stage 2: Containerization & CI/CD Pipelines", "duration": "5 weeks", "milestones": ["Create lightweight Docker images with multi-stage builds", "Build GitHub Actions automated testing and linting pipelines", "Push hardened images to container registries"]},
            {"title": "Stage 3: Kubernetes Cluster Orchestration", "duration": "6 weeks", "milestones": ["Deploy stateful and stateless applications on Kubernetes", "Configure Ingress controllers and TLS certificates", "Package complex applications with Helm charts"]},
            {"title": "Stage 4: Infrastructure as Code & Observability", "duration": "5 weeks", "milestones": ["Provision cloud clusters with Terraform", "Implement continuous deployment via ArgoCD GitOps", "Set up Prometheus metric scraping and Grafana alerts"]}
        ],
        "interview": [
            {"category": "Technical", "q": "What is the difference between a Container and a Virtual Machine?", "tip": "Containers share the host OS kernel and isolate user space (namespaces/cgroups), offering near-instant boot and low footprint. VMs virtualize hardware and run a full guest OS."},
            {"category": "Technical", "q": "Explain the difference between Rolling, Blue-Green, and Canary deployments.", "tip": "Rolling gradually replaces pods. Blue-Green swaps traffic between identical production environments via routing. Canary routes a small percentage of traffic to test stability."}
        ]
    },

    "Cybersecurity Analyst": {
        "icon": "🔐",
        "category": "Cybersecurity",
        "image": str(BASE_ASSETS / "cyber.png"),
        "tagline": "Protect corporate networks, defend endpoints, and respond to cyber threats.",
        "salary_range": "₹6L – ₹25L LPA (Est. India Market)",
        "salary_details": [
            {"level": "Junior SOC / Cyber Analyst", "salary": "₹6L – ₹9.5L LPA", "exp": "0–2 years"},
            {"level": "Mid-Level Security Analyst", "salary": "₹9.5L – ₹17L LPA", "exp": "2–5 years"},
            {"level": "Senior Security Consultant", "salary": "₹17L – ₹30L+ LPA", "exp": "5+ years"}
        ],
        "demand": "High Demand",
        "est_time": "6–8 months",
        "readiness_base": 30,
        "readiness_max": 88,
        "skills": [
            {"name": "Network Protocols & Traffic Analysis (Wireshark)", "current": 45, "required": 90},
            {"name": "Threat Hunting & SIEM (Splunk/ELK)", "current": 30, "required": 85},
            {"name": "Vulnerability Assessment (Nessus/Nmap)", "current": 35, "required": 85},
            {"name": "Incident Response & Forensics", "current": 25, "required": 80},
            {"name": "Security Compliance & ISO/NIST", "current": 35, "required": 75}
        ],
        "phases": [
            {"num": "Phase 1", "name": "Networking & System Security", "duration": "0 – 5 weeks", "tags": ["OSI Model", "TCP/IP", "Firewalls", "Linux Hardening", "Wireshark"]},
            {"num": "Phase 2", "name": "Threats & Vulnerability Scanning", "duration": "5 – 10 weeks", "tags": ["OWASP Top 10", "Nmap", "Nessus", "CVE Analysis", "Metasploit Basics"]},
            {"num": "Phase 3", "name": "Security Operations & SIEM", "duration": "10 – 16 weeks", "tags": ["Splunk", "Log Analysis", "SOC Playbooks", "Intrusion Detection (Snort)"]},
            {"num": "Phase 4", "name": "Digital Forensics & Governance", "duration": "16 – 22 weeks", "tags": ["Memory Forensics", "MITRE ATT&CK", "NIST Framework", "Incident Response"]}
        ],
        "resources": [
            {"name": "TryHackMe", "desc": "Gamified hands-on cybersecurity and defense labs", "type": "Platform", "cost": "Free / Paid", "url": "https://tryhackme.com"},
            {"name": "OverTheWire Wargames", "desc": "Practical command-line security wargames", "type": "Practice", "cost": "Free", "url": "https://overthewire.org"}
        ],
        "projects": [
            {"title": "Home Security Lab with Snort & Splunk", "difficulty": "Intermediate", "tech": ["Linux", "Snort", "Splunk", "VirtualBox"], "objectives": ["Simulated port scan detection", "Log forwarder setup", "Alert dashboard"]},
            {"title": "Corporate Vulnerability Assessment Report", "difficulty": "Intermediate", "tech": ["Nessus", "Nmap", "Markdown"], "objectives": ["Host discovery audit", "CVSS scoring", "Remediation roadmap"]}
        ],
        "stages": [
            {"title": "Stage 1: Core Networking & Protocol Inspection", "duration": "5 weeks", "milestones": ["Dissect TCP handshakes and DNS traffic with Wireshark", "Configure Linux iptables and UFW firewall rules", "Harden SSH servers against brute force attempts"]},
            {"title": "Stage 2: Threat Detection & Vulnerability Auditing", "duration": "5 weeks", "milestones": ["Conduct network port scans using Nmap flags", "Identify outdated services and map to CVE records", "Scan web applications against OWASP vulnerabilities"]},
            {"title": "Stage 3: Security Operations Center (SOC) & SIEM", "duration": "5 weeks", "milestones": ["Ingest authentication and access logs into Splunk", "Write detection alert rules for lateral movement", "Execute incident response playbooks for phishing alerts"]},
            {"title": "Stage 4: Forensics & Incident Containment", "duration": "5 weeks", "milestones": ["Analyze malware memory dumps using Volatility", "Map attacks to the MITRE ATT&CK enterprise matrix", "Draft post-incident forensic root cause reports"]}
        ],
        "interview": [
            {"category": "Technical", "q": "Explain the CIA Triad with real-world technical examples for each component.", "tip": "Confidentiality (encryption, RBAC), Integrity (hashing, digital signatures), Availability (DDoS mitigation, redundancy)."},
            {"category": "Technical", "q": "What is the difference between asymmetric and symmetric encryption?", "tip": "Symmetric uses one shared secret key for encryption and decryption (fast, e.g., AES). Asymmetric uses a public-private key pair (key exchange, e.g., RSA/ECC)."}
        ]
    },

    "Ethical Hacker": {
        "icon": "👨‍💻",
        "category": "Cybersecurity",
        "image": str(BASE_ASSETS / "ethical.png"),
        "tagline": "Perform penetration testing, discover system zero-days, and secure attack vectors.",
        "salary_range": "₹7L – ₹22L LPA (Est. India Market)",
        "salary_details": [
            {"level": "Junior Penetration Tester", "salary": "₹7L – ₹10L LPA", "exp": "0–2 years"},
            {"level": "Penetration Tester / Red Teamer", "salary": "₹10L – ₹18L LPA", "exp": "2–5 years"},
            {"level": "Senior Principal Security Auditor", "salary": "₹18L – ₹30L+ LPA", "exp": "5+ years"}
        ],
        "demand": "High Demand",
        "est_time": "6–9 months",
        "readiness_base": 25,
        "readiness_max": 88,
        "skills": [
            {"name": "Web Application Penetration Testing (Burp Suite)", "current": 40, "required": 95},
            {"name": "Network Reconnaissance & Exploitation", "current": 35, "required": 90},
            {"name": "Python / Bash Exploit Scripting", "current": 40, "required": 85},
            {"name": "Privilege Escalation (Linux/Windows)", "current": 20, "required": 85},
            {"name": "OWASP Testing Methodologies", "current": 35, "required": 90}
        ],
        "phases": [
            {"num": "Phase 1", "name": "Recon & Scripting", "duration": "0 – 5 weeks", "tags": ["Kali Linux", "Bash", "Python", "OSINT", "Nmap"]},
            {"num": "Phase 2", "name": "Web Pentesting", "duration": "5 – 11 weeks", "tags": ["Burp Suite", "SQL Injection", "XSS", "SSRF", "IDOR"]},
            {"num": "Phase 3", "name": "Network & Privilege Escalation", "duration": "11 – 17 weeks", "tags": ["Metasploit", "SUID Escalation", "Active Directory", "Kerberoasting"]},
            {"num": "Phase 4", "name": "Reporting & Bug Bounty", "duration": "17 – 24 weeks", "tags": ["HackerOne", "Remediation Proofs", "CVSS", "Professional Audits"]}
        ],
        "resources": [
            {"name": "PortSwigger Web Security Academy", "desc": "Free interactive web penetration testing labs by makers of Burp Suite", "type": "Labs", "cost": "Free", "url": "https://portswigger.net/web-security"},
            {"name": "Hack The Box", "desc": "Challenging simulated virtual machines and red teaming", "type": "Platform", "cost": "Free / Paid", "url": "https://www.hackthebox.com"}
        ],
        "projects": [
            {"title": "Automated Subdomain Reconnaissance Tool", "difficulty": "Intermediate", "tech": ["Python", "DNS", "APIs"], "objectives": ["Certificate transparency search", "Port validation", "Slack alert"]},
            {"title": "Comprehensive Pentest Report for Vulnerable Web App", "difficulty": "Advanced", "tech": ["Burp Suite", "SQLMap", "Markdown"], "objectives": ["Exploit reproduction", "Severity scoring", "Defensive mitigation"]}
        ],
        "stages": [
            {"title": "Stage 1: Reconnaissance & Environment Setup", "duration": "5 weeks", "milestones": ["Set up customized Kali Linux penetration environments", "Execute passive and active OSINT information gathering", "Automate port enumeration using Python scripts"]},
            {"title": "Stage 2: Web Application Security Assessment", "duration": "6 weeks", "milestones": ["Intercept and modify HTTP traffic using Burp Suite", "Exploit SQL Injections and cross-site scripting vulnerabilities", "Identify Insecure Direct Object References (IDORs)"]},
            {"title": "Stage 3: Privilege Escalation & Lateral Movement", "duration": "6 weeks", "milestones": ["Exploit misconfigured SUID binaries in Linux", "Enumerate Windows Active Directory domain policies", "Capture and crack password hashes using Hashcat"]},
            {"title": "Stage 4: Professional Reporting & Bug Bounty", "duration": "5 weeks", "milestones": ["Format penetration reports with CVSS score matrices", "Document clear reproduction steps for development teams", "Participate in responsible bug bounty disclosures"]}
        ],
        "interview": [
            {"category": "Technical", "q": "Explain the difference between Stored, Reflected, and DOM-based Cross-Site Scripting (XSS).", "tip": "Stored persists in DB and executes for every visitor. Reflected bounces off server via query param. DOM modifies client DOM in browser directly without server reflection."},
            {"category": "Technical", "q": "How does a Blind SQL Injection differ from an in-band SQL Injection?", "tip": "In-band returns data directly in the HTTP response. Blind yields no direct output; you infer data via boolean true/false responses or deliberate time delays (SLEEP)."}
        ]
    },

    "UI Designer": {
        "icon": "🎨",
        "category": "UI / UX Design",
        "image": str(BASE_ASSETS / "uid.png"),
        "tagline": "Craft pixel-perfect visual designs, design systems, and delightful digital user interfaces.",
        "salary_range": "₹4L – ₹15L LPA (Est. India Market)",
        "salary_details": [
            {"level": "Junior UI Designer", "salary": "₹4L – ₹6.5L LPA", "exp": "0–2 years"},
            {"level": "Mid-Level UI Designer", "salary": "₹6.5L – ₹12L LPA", "exp": "2–4 years"},
            {"level": "Senior UI / Visual Design Lead", "salary": "₹12L – ₹22L+ LPA", "exp": "4+ years"}
        ],
        "demand": "Growing",
        "est_time": "3–5 months",
        "readiness_base": 45,
        "readiness_max": 95,
        "skills": [
            {"name": "Figma Mastery (Auto Layout, Variants)", "current": 65, "required": 95},
            {"name": "Design Systems & Token Architecture", "current": 40, "required": 90},
            {"name": "Typography, Color Theory & Hierarchy", "current": 60, "required": 90},
            {"name": "Micro-Interactions & Prototyping", "current": 40, "required": 85},
            {"name": "Responsive Breakpoints & Developer Handoff", "current": 50, "required": 85}
        ],
        "phases": [
            {"num": "Phase 1", "name": "Visual Design Principles", "duration": "0 – 4 weeks", "tags": ["Color Harmony", "Typography Hierarchy", "Grid Systems", "Visual Weight"]},
            {"num": "Phase 2", "name": "Figma Advanced Tools", "duration": "4 – 8 weeks", "tags": ["Auto Layout", "Component Sets", "Interactive Variants", "Figma Variables"]},
            {"num": "Phase 3", "name": "Design Systems & UI Kits", "duration": "8 – 12 weeks", "tags": ["Design Tokens", "Accessibility (WCAG)", "Button States", "Form Components"]},
            {"num": "Phase 4", "name": "Micro-Interactions & Handoff", "duration": "12 – 16 weeks", "tags": ["Smart Animate", "Interactive Prototypes", "Dev Handoff", "Portfolio Showcase"]}
        ],
        "resources": [
            {"name": "Figma Learn & Community", "desc": "Official Figma design guides and design system templates", "type": "Platform", "cost": "Free", "url": "https://help.figma.com/hc/en-us/categories/360002051613-Learn-design"},
            {"name": "Refactoring UI by Adam Wathan & Steve Schoger", "desc": "Actionable design tactics for developers and designers", "type": "Book", "cost": "Paid", "url": "https://www.refactoringui.com"}
        ],
        "projects": [
            {"title": "FinTech Mobile Banking Design System", "difficulty": "Intermediate", "tech": ["Figma", "Design Tokens", "Auto Layout"], "objectives": ["Dark and light modes", "Interactive balance charts", "Comprehensive component kit"]},
            {"title": "SaaS Analytics Dashboard UI Overhaul", "difficulty": "Intermediate", "tech": ["Figma", "Smart Animate"], "objectives": ["Complex table controls", "Micro-interactions", "Developer redlines"]}
        ],
        "stages": [
            {"title": "Stage 1: Visual Design Theory & Layout Rules", "duration": "3 weeks", "milestones": ["Apply 8pt grid systems across desktop and mobile layouts", "Establish proportional typography scales", "Select accessible color palettes meeting WCAG AA standards"]},
            {"title": "Stage 2: Advanced Figma Components", "duration": "4 weeks", "milestones": ["Build nested auto-layout component cards", "Create stateful variants (hover, active, disabled)", "Leverage Figma variables for multi-theme switching"]},
            {"title": "Stage 3: Scalable Design Systems", "duration": "4 weeks", "milestones": ["Publish a centralized design system library", "Define semantic design tokens for spacing and colors", "Conduct accessibility contrast compliance checks"]},
            {"title": "Stage 4: High-Fidelity Prototyping & Handoff", "duration": "4 weeks", "milestones": ["Animate realistic micro-interactions using Smart Animate", "Prepare asset exports and code token specs for engineers", "Publish design portfolio case studies on Behance/Dribbble"]}
        ],
        "interview": [
            {"category": "Technical", "q": "What is an 8-point grid system, and why is it preferred by digital product designers?", "tip": "Explain scaling across varying screen densities (0.5x, 1x, 2x, 3x) without sub-pixel rendering blur, and consistent rhythm for engineering handoff."},
            {"category": "Case", "q": "How do you ensure a design system remains scalable and doesn't get cluttered as a company grows?", "tip": "Governance workflows, token abstraction, component deprecation cycles, and bi-weekly syncs with frontend engineering teams."}
        ]
    },

    "UX Designer": {
        "icon": "✨",
        "category": "UI / UX Design",
        "image": str(BASE_ASSETS / "uxd.png"),
        "tagline": "Conduct user research, map user journeys, and solve usability friction in digital products.",
        "salary_range": "₹5L – ₹18L LPA (Est. India Market)",
        "salary_details": [
            {"level": "Junior UX Researcher/Designer", "salary": "₹5L – ₹8L LPA", "exp": "0–2 years"},
            {"level": "Mid-Level UX Designer", "salary": "₹8L – ₹15L LPA", "exp": "2–5 years"},
            {"level": "Senior UX Lead / Strategist", "salary": "₹15L – ₹28L+ LPA", "exp": "5+ years"}
        ],
        "demand": "Growing",
        "est_time": "4–6 months",
        "readiness_base": 40,
        "readiness_max": 92,
        "skills": [
            {"name": "User Research & Qualitative Interviews", "current": 55, "required": 90},
            {"name": "Information Architecture & Wireframing", "current": 60, "required": 90},
            {"name": "Usability Testing & Heuristic Evaluation", "current": 40, "required": 85},
            {"name": "User Journey Mapping & Personas", "current": 50, "required": 85},
            {"name": "Quantitative Product Analytics (Hotjar/Mixpanel)", "current": 30, "required": 75}
        ],
        "phases": [
            {"num": "Phase 1", "name": "UX Research Methods", "duration": "0 – 4 weeks", "tags": ["User Interviews", "Surveys", "Persona Creation", "Empathy Maps"]},
            {"num": "Phase 2", "name": "Information Architecture", "duration": "4 – 8 weeks", "tags": ["Card Sorting", "User Flows", "Sitemaps", "Low-Fidelity Wireframes"]},
            {"num": "Phase 3", "name": "Usability Testing", "duration": "8 – 12 weeks", "tags": ["Nielsen Norman Heuristics", "Moderated Testing", "Task Completion Rates"]},
            {"num": "Phase 4", "name": "Case Study & Product Strategy", "duration": "12 – 18 weeks", "tags": ["Metrics (SUS, CSAT)", "A/B Testing", "Portfolio Case Study Writing"]}
        ],
        "resources": [
            {"name": "Nielsen Norman Group Articles & Videos", "desc": "Evidence-based user experience research authority", "type": "Articles", "cost": "Free", "url": "https://www.nngroup.com/articles/"},
            {"name": "LawsofUX.com", "desc": "Collection of psychological heuristics applicable to design", "type": "Reference", "cost": "Free", "url": "https://lawsofux.com"}
        ],
        "projects": [
            {"title": "Healthcare App Patient Booking Usability Redesign", "difficulty": "Intermediate", "tech": ["Figma", "User Interviews", "Miro"], "objectives": ["Identify booking drop-off", "Heuristic audit", "Validated redesign"]},
            {"title": "E-Commerce Checkout Flow Friction Teardown", "difficulty": "Intermediate", "tech": ["Usability Testing", "User Journey Map"], "objectives": ["Cart abandonment analysis", "Task timing comparison", "Case study"]}
        ],
        "stages": [
            {"title": "Stage 1: User Discovery & Empathy Mapping", "duration": "4 weeks", "milestones": ["Conduct 5+ semi-structured qualitative user interviews", "Synthesize findings into archetypal user personas", "Map emotional customer journey phases and friction points"]},
            {"title": "Stage 2: Information Architecture & Rapid Wireframing", "duration": "4 weeks", "milestones": ["Perform open and closed card sorting exercises", "Draft hierarchical application sitemaps", "Sketch rapid low-fidelity paper and digital wireframes"]},
            {"title": "Stage 3: Usability Auditing & Heuristic Evaluation", "duration": "4 weeks", "milestones": ["Evaluate applications against Jakob Nielsen's 10 Usability Heuristics", "Conduct moderated usability test sessions with target users", "Calculate System Usability Scale (SUS) scores"]},
            {"title": "Stage 4: Product Metrics & Portfolio Writing", "duration": "4 weeks", "milestones": ["Quantify redesign success with Task Completion Time improvements", "Document problem-to-solution narrative case studies", "Publish comprehensive UX research presentations"]}
        ],
        "interview": [
            {"category": "Case", "q": "Walk me through a project where your research invalidated an initial assumption made by the product team.", "tip": "Describe the initial bias, the research methodology chosen, the surprising data gathered, and how you steered stakeholders toward a user-centric compromise."},
            {"category": "Technical", "q": "Explain Hick's Law and Fitts's Law with digital product examples.", "tip": "Hick's Law: Time to decide increases with number and complexity of choices (simplify navigation). Fitts's Law: Time to hit a target depends on distance and size (large, close CTAs)."}
        ]
    },

    "Product Manager": {
        "icon": "📦",
        "category": "Management & Delivery",
        "image": str(BASE_ASSETS / "prod.png"),
        "tagline": "Define product strategy, align cross-functional engineering and design, and drive business ROI.",
        "salary_range": "₹10L – ₹40L LPA (Est. India Market)",
        "salary_details": [
            {"level": "Associate Product Manager", "salary": "₹10L – ₹15L LPA", "exp": "0–2 years"},
            {"level": "Product Manager", "salary": "₹15L – ₹26L LPA", "exp": "2–5 years"},
            {"level": "Senior Product Manager", "salary": "₹26L – ₹42L+ LPA", "exp": "5–8 years"},
            {"level": "Director / Head of Product", "salary": "₹42L – ₹70L+ LPA", "exp": "8+ years"}
        ],
        "demand": "Growing",
        "est_time": "4–6 months",
        "readiness_base": 40,
        "readiness_max": 92,
        "skills": [
            {"name": "Product Strategy & Roadmapping", "current": 55, "required": 90},
            {"name": "PRD (Product Requirement Documents)", "current": 60, "required": 95},
            {"name": "Data Analytics & North Star Metrics", "current": 45, "required": 85},
            {"name": "Agile / Scrum Delivery (Jira)", "current": 65, "required": 90},
            {"name": "Customer Discovery & Market Sizing", "current": 40, "required": 85}
        ],
        "phases": [
            {"num": "Phase 1", "name": "Product Fundamentals", "duration": "0 – 4 weeks", "tags": ["Product Lifecycle", "Problem Space vs Solution Space", "Customer Interviews"]},
            {"num": "Phase 2", "name": "Documentation & Execution", "duration": "4 – 8 weeks", "tags": ["PRD Writing", "User Stories", "Acceptance Criteria", "Scrum Framework"]},
            {"num": "Phase 3", "name": "Product Analytics & Growth", "duration": "8 – 12 weeks", "tags": ["North Star Metric", "A/B Testing", "Funnel Optimization", "Cohort Retention"]},
            {"num": "Phase 4", "name": "Go-To-Market & Strategy", "duration": "12 – 18 weeks", "tags": ["Pricing Models", "GTM Strategy", "Competitive Moats", "Portfolio Teardowns"]}
        ],
        "resources": [
            {"name": "Lenny's Newsletter & Podcast", "desc": "Top product, growth, and management wisdom from Silicon Valley", "type": "Newsletter", "cost": "Free / Paid", "url": "https://www.lennysnewsletter.com"},
            {"name": "Inspired by Marty Cagan", "desc": "Seminal foundational book on technology product management", "type": "Book", "cost": "Paid", "url": "https://svpg.com/books/inspired-how-to-create-tech-products-customers-love/"}
        ],
        "projects": [
            {"title": "B2B SaaS Feature Launch PRD", "difficulty": "Intermediate", "tech": ["Notion", "Figma", "Jira"], "objectives": ["Problem statement & customer evidence", "Scope trade-offs & milestones", "Success KPIs"]},
            {"title": "FinTech App Onboarding Funnel Teardown", "difficulty": "Intermediate", "tech": ["Mixpanel", "Analytics"], "objectives": ["Funnel step drop-off analysis", "A/B hypothesis formulation", "ROI justification"]}
        ],
        "stages": [
            {"title": "Stage 1: Problem Discovery & Customer Validation", "duration": "4 weeks", "milestones": ["Conduct discovery interviews to validate unmet customer needs", "Calculate Total Addressable Market (TAM) estimates", "Differentiate pain points from superficial feature requests"]},
            {"title": "Stage 2: Crisp PRD Authoring & Engineering Alignment", "duration": "4 weeks", "milestones": ["Author comprehensive Product Requirement Documents", "Write unambiguous user stories with strict acceptance criteria", "Facilitate sprint grooming and backlog prioritization"]},
            {"title": "Stage 3: Product Metrics & Experimentation", "duration": "4 weeks", "milestones": ["Define North Star and input KPI trees", "Design scientifically rigorous A/B testing experiment specs", "Analyze funnel drop-offs using cohort tracking"]},
            {"title": "Stage 4: Go-To-Market & Executive Alignment", "duration": "4 weeks", "milestones": ["Craft cohesive Go-To-Market (GTM) launch plans", "Align sales, marketing, and customer success teams", "Defend roadmap trade-offs using data-backed frameworks"]}
        ],
        "interview": [
            {"category": "Case", "q": "How would you improve Google Maps for daily office commuters in high-traffic metro cities?", "tip": "Structure clearly: User segments (commuters), top pain points (delays, parking, transit integration), 3 creative solutions, prioritize via RICE framework, define metrics."},
            {"category": "Case", "q": "Spotify sees a 5% drop in weekly playlist creations. How would you investigate and act on this?", "tip": "Diagnose root cause (technical bug vs external seasonality vs design changes), segment users, hypothesize solutions, test with minimum viable experiments."}
        ]
    },

    "Project Manager": {
        "icon": "📋",
        "category": "Management & Delivery",
        "image": str(BASE_ASSETS / "proj.png"),
        "tagline": "Coordinate timelines, manage risks, balance resources, and ensure punctual milestone delivery.",
        "salary_range": "₹8L – ₹25L LPA (Est. India Market)",
        "salary_details": [
            {"level": "Junior Project Coordinator", "salary": "₹8L – ₹11L LPA", "exp": "0–2 years"},
            {"level": "Technical Project Manager", "salary": "₹11L – ₹19L LPA", "exp": "2–5 years"},
            {"level": "Senior Program Manager / Delivery Head", "salary": "₹19L – ₹30L+ LPA", "exp": "5+ years"}
        ],
        "demand": "Stable",
        "est_time": "4–6 months",
        "readiness_base": 45,
        "readiness_max": 90,
        "skills": [
            {"name": "Agile / Scrum / Kanban Methodologies", "current": 70, "required": 95},
            {"name": "Risk Management & Mitigation", "current": 45, "required": 90},
            {"name": "Budget & Resource Planning", "current": 40, "required": 85},
            {"name": "Jira, Confluence & Asana Mastery", "current": 60, "required": 90},
            {"name": "Stakeholder Communication & Status Reporting", "current": 55, "required": 90}
        ],
        "phases": [
            {"num": "Phase 1", "name": "Project Lifecycle & Methodologies", "duration": "0 – 4 weeks", "tags": ["Waterfall vs Agile", "Scrum Roles", "Kanban WIP", "Sprint Cadence"]},
            {"num": "Phase 2", "name": "Planning & Estimations", "duration": "4 – 8 weeks", "tags": ["WBS Breakdown", "Critical Path Method", "Story Points", "Planning Poker"]},
            {"num": "Phase 3", "name": "Risk & Stakeholder Management", "duration": "8 – 12 weeks", "tags": ["RAID Logs", "Risk Matrices", "Steering Committees", "Escalation Paths"]},
            {"num": "Phase 4", "name": "Tooling & Delivery Tracking", "duration": "12 – 16 weeks", "tags": ["Jira Advanced Roadmaps", "Burndown Charts", "PMP/CAPM Prep", "Retrospectives"]}
        ],
        "resources": [
            {"name": "Scrum Guide by Ken Schwaber & Jeff Sutherland", "desc": "The definitive rulebook of Scrum framework", "type": "Guide", "cost": "Free", "url": "https://scrumguides.org"},
            {"name": "Project Management Institute (PMI)", "desc": "Standard guidelines, PMBOK concepts, and certifications", "type": "Platform", "cost": "Paid", "url": "https://www.pmi.org"}
        ],
        "projects": [
            {"title": "Enterprise Cloud Migration Project Plan", "difficulty": "Intermediate", "tech": ["Jira", "Confluence", "Gantt Charts"], "objectives": ["Phase-gate timelines", "Resource allocation matrix", "Disaster recovery rollback contingency"]},
            {"title": "Multi-Team RAID Log & Escalation Matrix", "difficulty": "Intermediate", "tech": ["Excel/Notion", "Risk Matrix"], "objectives": ["Risks, Assumptions, Issues, Dependencies tracking", "Mitigation owners"]}
        ],
        "stages": [
            {"title": "Stage 1: Delivery Frameworks & Ceremonies", "duration": "4 weeks", "milestones": ["Facilitate sprint planning, daily standups, and retrospectives", "Enforce work-in-progress (WIP) limits in Kanban systems", "Calculate team velocity and sprint capacities"]},
            {"title": "Stage 2: Timeline Scheduling & Resource Allocation", "duration": "4 weeks", "milestones": ["Create Work Breakdown Structures (WBS) for complex deliverables", "Identify project bottlenecks with Critical Path Analysis", "Resolve conflicting engineering resource demands"]},
            {"title": "Stage 3: Risk Management & RAID Tracking", "duration": "4 weeks", "milestones": ["Maintain live RAID logs for executive visibility", "Assign probability and impact scores to operational blockers", "Enact timely mitigation strategies before deadlines slip"]},
            {"title": "Stage 4: Executive Reporting & Project Closeout", "duration": "4 weeks", "milestones": ["Build automated Burndown and Burnup velocity charts", "Deliver concise weekly status updates to leadership", "Conduct post-mortem reviews and capture lessons learned"]}
        ],
        "interview": [
            {"category": "Case", "q": "Your lead engineer tells you a critical feature is 2 weeks behind schedule with only 5 days left before release. How do you handle this?", "tip": "Assess scope immediately: Can non-critical sub-components be phased? Communicate transparently with stakeholders early. Do not burn out team."},
            {"category": "Behavioral", "q": "How do you manage conflict between a product manager demanding new features and engineering pushing for technical debt refactoring?", "tip": "Use a balanced allocation model (e.g. 70% features, 20% tech debt, 10% bugs) agreed upon beforehand with executive sponsorship."}
        ]
    },

    "QA Engineer": {
        "icon": "🧪",
        "category": "Quality Assurance & Testing",
        "image": str(BASE_ASSETS / "qa.png"),
        "tagline": "Guarantee software reliability through comprehensive manual testing, test plans, and bug lifecycle.",
        "salary_range": "₹4L – ₹14L LPA (Est. India Market)",
        "salary_details": [
            {"level": "Junior QA Engineer (0–2 yrs)", "salary": "₹4L – ₹6.5L LPA", "exp": "0–2 years"},
            {"level": "Senior QA Engineer (2–5 yrs)", "salary": "₹6.5L – ₹12L LPA", "exp": "2–5 years"},
            {"level": "QA Lead / Quality Manager (5+ yrs)", "salary": "₹12L – ₹20L+ LPA", "exp": "5+ years"}
        ],
        "demand": "Stable",
        "est_time": "3–4 months",
        "readiness_base": 50,
        "readiness_max": 95,
        "skills": [
            {"name": "Test Case Design & Test Plans", "current": 70, "required": 95},
            {"name": "API Testing (Postman/Curl)", "current": 55, "required": 90},
            {"name": "Bug Tracking & Triage (Jira)", "current": 65, "required": 90},
            {"name": "Database Verification (SQL)", "current": 45, "required": 85},
            {"name": "Regression & Exploratory Testing", "current": 60, "required": 90}
        ],
        "phases": [
            {"num": "Phase 1", "name": "QA Fundamentals", "duration": "0 – 3 weeks", "tags": ["STLC", "Test Scenarios", "Boundary Value Analysis", "Equivalence Partitioning"]},
            {"num": "Phase 2", "name": "API & Integration Testing", "duration": "3 – 6 weeks", "tags": ["Postman", "HTTP Headers", "Payload Validation", "Auth Tokens"]},
            {"num": "Phase 3", "name": "Database & Security Checks", "duration": "6 – 10 weeks", "tags": ["SQL Verification", "Data Integrity", "Session Security", "Cross-Browser Testing"]},
            {"num": "Phase 4", "name": "Test Automation Exposure", "duration": "10 – 14 weeks", "tags": ["Cypress Basics", "Selenium Intro", "CI Test Reports", "ISTQB Concepts"]}
        ],
        "resources": [
            {"name": "Ministry of Testing", "desc": "Global community articles, test challenges, and tutorials", "type": "Community", "cost": "Free", "url": "https://www.ministryoftesting.com"},
            {"name": "Postman Learning Center", "desc": "Complete API testing, scripting, and automation guides", "type": "Documentation", "cost": "Free", "url": "https://learning.postman.com"}
        ],
        "projects": [
            {"title": "E-Commerce Checkout Test Plan & Matrix", "difficulty": "Beginner", "tech": ["TestRail/Sheets", "Jira"], "objectives": ["Boundary value payment edge cases", "Cross-browser matrix", "Bug reports with video logs"]},
            {"title": "Comprehensive Postman API Test Suite", "difficulty": "Intermediate", "tech": ["Postman", "JavaScript Assertions"], "objectives": ["Automated status code checks", "Schema validation", "Chained request tokens"]}
        ],
        "stages": [
            {"title": "Stage 1: Software Testing Life Cycle (STLC)", "duration": "3 weeks", "milestones": ["Author detailed test plans and acceptance test scenarios", "Apply Boundary Value Analysis and Equivalence Partitioning", "Log clear, reproducible bug tickets with step-by-step logs"]},
            {"title": "Stage 2: API Testing & Contract Verification", "duration": "4 weeks", "milestones": ["Test REST endpoints across positive and negative payload cases", "Validate response JSON schemas and HTTP header constraints", "Automate Postman test collections with pre-request scripts"]},
            {"title": "Stage 3: Database & Security Integrity Testing", "duration": "4 weeks", "milestones": ["Execute SQL queries to verify persistent backend data mutations", "Audit web sessions for cookie security and expiration", "Validate international localization and currency rounding"]},
            {"title": "Stage 4: Regression Strategy & Test Management", "duration": "3 weeks", "milestones": ["Maintain regression test suites for rapid release cycles", "Conduct risk-based exploratory testing sessions", "Draft sign-off quality readiness certificates"]}
        ],
        "interview": [
            {"category": "Technical", "q": "What is the difference between Smoke Testing, Sanity Testing, and Regression Testing?", "tip": "Smoke verifies basic critical functionality after a new build. Sanity verifies specific bug fixes. Regression confirms new code didn't break existing features."},
            {"category": "Case", "q": "How would you design test cases for a coffee vending machine?", "tip": "Cover functional (money inserted, drink dispensed, correct change), negative (invalid coins, empty ingredients), performance (consecutive requests), and physical safety."}
        ]
    },

    "Automation Tester": {
        "icon": "⚡",
        "category": "Quality Assurance & Testing",
        "image": str(BASE_ASSETS / "automation.png"),
        "tagline": "Build scalable automated test frameworks for web, mobile, and APIs with CI/CD integration.",
        "salary_range": "₹5L – ₹18L LPA (Est. India Market)",
        "salary_details": [
            {"level": "Junior Automation Engineer", "salary": "₹5L – ₹8.5L LPA", "exp": "0–2 years"},
            {"level": "SDET / Automation Engineer", "salary": "₹8.5L – ₹15L LPA", "exp": "2–5 years"},
            {"level": "Lead SDET / Automation Architect", "salary": "₹15L – ₹25L+ LPA", "exp": "5+ years"}
        ],
        "demand": "High Demand",
        "est_time": "4–6 months",
        "readiness_base": 40,
        "readiness_max": 92,
        "skills": [
            {"name": "Playwright / Cypress / Selenium", "current": 45, "required": 90},
            {"name": "Python or Java or TypeScript for QA", "current": 50, "required": 85},
            {"name": "Page Object Model (POM) Architecture", "current": 35, "required": 90},
            {"name": "API Automation (RestAssured / Pytest)", "current": 40, "required": 85},
            {"name": "CI/CD Pipeline Integration (GitHub Actions)", "current": 30, "required": 80}
        ],
        "phases": [
            {"num": "Phase 1", "name": "Programming Foundations", "duration": "0 – 4 weeks", "tags": ["Python or TS", "OOP Principles", "Data Structures", "Pytest / Jest"]},
            {"num": "Phase 2", "name": "Modern UI Automation", "duration": "4 – 9 weeks", "tags": ["Playwright", "Locators", "Waits & Timeouts", "Page Object Model"]},
            {"num": "Phase 3", "name": "API & Database Automation", "duration": "9 – 13 weeks", "tags": ["Requests / RestAssured", "JSON Schema Validation", "Database Assertion"]},
            {"num": "Phase 4", "name": "Scale & CI/CD Pipelines", "duration": "13 – 18 weeks", "tags": ["Parallel Execution", "Docker Test Runners", "Allure Reports", "GitHub Actions"]}
        ],
        "resources": [
            {"name": "Playwright Official Documentation", "desc": "Modern end-to-end testing documentation and guides", "type": "Documentation", "cost": "Free", "url": "https://playwright.dev"},
            {"name": "Test Automation University", "desc": "Free world-class courses by top test automation leaders", "type": "Course", "cost": "Free", "url": "https://testautomationu.applitools.com"}
        ],
        "projects": [
            {"title": "Full-Stack Playwright Automation Framework", "difficulty": "Intermediate", "tech": ["Playwright", "TypeScript", "Page Object Model"], "objectives": ["Cross-browser testing (Chromium/Firefox/WebKit)", "Parallel execution", "HTML report artifact"]},
            {"title": "Automated API Test Suite with Pytest", "difficulty": "Intermediate", "tech": ["Python", "Pytest", "Requests"], "objectives": ["Token lifecycle fixtures", "Negative payload tests", "Allure reporting"]}
        ],
        "stages": [
            {"title": "Stage 1: Test Automation Scripting & OOP", "duration": "4 weeks", "milestones": ["Master object-oriented programming for test maintainability", "Configure test runners, fixtures, and assertions", "Implement robust locator strategies (CSS, XPath, accessibility IDs)"]},
            {"title": "Stage 2: Web Test Automation with Playwright", "duration": "5 weeks", "milestones": ["Architect clean Page Object Models (POM)", "Eliminate flaky tests with auto-waiting assertions", "Simulate network throttling and mock API responses"]},
            {"title": "Stage 3: Automated API & Database Verification", "duration": "4 weeks", "milestones": ["Build automated REST request suites with status and payload checks", "Execute setup/teardown database state seeding", "Validate JSON schema contracts automatically"]},
            {"title": "Stage 4: Distributed Cloud Execution & CI/CD", "duration": "5 weeks", "milestones": ["Integrate test suite execution into GitHub Actions", "Run tests concurrently across Docker containers", "Generate interactive visual Allure test reports"]}
        ],
        "interview": [
            {"category": "Technical", "q": "What is the Page Object Model (POM), and why is it essential in test automation?", "tip": "Explain separation of test logic from UI selectors. If a button locator changes, you update only one page class rather than hundreds of individual tests."},
            {"category": "Technical", "q": "How do you handle and eliminate flaky tests in an automated test pipeline?", "tip": "Avoid hardcoded sleeps; use explicit dynamic conditions. Isolate test data per test, mock unstable third-party APIs, and trace network calls."}
        ]
    },

    "Database Administrator": {
        "icon": "🗄️",
        "category": "Database Administration",
        "image": str(BASE_ASSETS / "data.png"),
        "tagline": "Manage, tune, secure, and ensure 99.99% availability for mission-critical enterprise databases.",
        "salary_range": "₹6L – ₹20L LPA (Est. India Market)",
        "salary_details": [
            {"level": "Junior Database Admin", "salary": "₹6L – ₹9L LPA", "exp": "0–2 years"},
            {"level": "Database Administrator (2–5 yrs)", "salary": "₹9L – ₹16L LPA", "exp": "2–5 years"},
            {"level": "Senior Lead DBA / Data Architect", "salary": "₹16L – ₹28L+ LPA", "exp": "5+ years"}
        ],
        "demand": "Stable",
        "est_time": "5–7 months",
        "readiness_base": 35,
        "readiness_max": 90,
        "skills": [
            {"name": "PostgreSQL & MySQL Administration", "current": 55, "required": 95},
            {"name": "Query Optimization & Performance Tuning", "current": 40, "required": 90},
            {"name": "High Availability & Replication", "current": 30, "required": 85},
            {"name": "Backup, Point-In-Time Recovery & Security", "current": 45, "required": 90},
            {"name": "Database Monitoring & Sharding", "current": 30, "required": 80}
        ],
        "phases": [
            {"num": "Phase 1", "name": "DB Architecture", "duration": "0 – 4 weeks", "tags": ["Storage Engines", "Buffer Pool", "WAL Logs", "Configuration Parameters"]},
            {"num": "Phase 2", "name": "Performance Tuning", "duration": "4 – 9 weeks", "tags": ["EXPLAIN ANALYZE", "B-Tree / GIN Indexes", "Lock Contention", "Connection Pooling"]},
            {"num": "Phase 3", "name": "High Availability & Replication", "duration": "9 – 14 weeks", "tags": ["Streaming Replication", "Read Replicas", "Failover", "PgBouncer"]},
            {"num": "Phase 4", "name": "Security & Disaster Recovery", "duration": "14 – 20 weeks", "tags": ["Point-in-Time Recovery", "TDE Encryption", "Auditing", "Automated Backups"]}
        ],
        "resources": [
            {"name": "PostgreSQL Official Documentation", "desc": "Internals, server administration, and configuration manuals", "type": "Documentation", "cost": "Free", "url": "https://www.postgresql.org/docs/"},
            {"name": "Use The Index, Luke!", "desc": "A guide to database performance for developers and DBAs", "type": "Guide", "cost": "Free", "url": "https://use-the-index-luke.com"}
        ],
        "projects": [
            {"title": "PostgreSQL Primary-Replica Cluster with Automatic Failover", "difficulty": "Advanced", "tech": ["PostgreSQL", "Patroni / Keepalived", "Docker"], "objectives": ["Synchronous streaming replication", "Automated leader election", "Zero data loss"]},
            {"title": "Slow Query Auditing & Index Optimization Package", "difficulty": "Intermediate", "tech": ["pg_stat_statements", "SQL"], "objectives": ["Identify top 10 bottleneck queries", "Index restructuring", "90% latency reduction"]}
        ],
        "stages": [
            {"title": "Stage 1: Storage Internals & Configuration", "duration": "4 weeks", "milestones": ["Tune shared_buffers, work_mem, and WAL write checkpoints", "Configure roles, table privileges, and network pg_hba.conf rules", "Monitor disk I/O throughput and table bloat"]},
            {"title": "Stage 2: Query Optimization & Indexing", "duration": "5 weeks", "milestones": ["Analyze query execution trees with EXPLAIN (ANALYZE, BUFFERS)", "Select between B-Tree, Hash, GIN, and BRIN indexes", "Eliminate deadlocks and mitigate row lock contention"]},
            {"title": "Stage 3: Replication & Connection Pooling", "duration": "5 weeks", "milestones": ["Set up streaming replication to multiple read replicas", "Deploy PgBouncer for high-concurrency client pooling", "Configure automated failover orchestrations"]},
            {"title": "Stage 4: Disaster Recovery & Security Hardening", "duration": "5 weeks", "milestones": ["Execute consistent Point-in-Time Recovery (PITR) from WAL archives", "Enforce encryption-at-rest and TLS in-flight encryption", "Automate backup validation and integrity testing"]}
        ],
        "interview": [
            {"category": "Technical", "q": "What is Write-Ahead Logging (WAL), and how does it guarantee durability (the 'D' in ACID)?", "tip": "Changes are written sequentially to the WAL disk log before being flushed to database data pages. On crash, the database replays WAL to recover consistent state."},
            {"category": "Technical", "q": "What causes table bloat in PostgreSQL, and how does VACUUM resolve it?", "tip": "MVCC creates new row versions on UPDATE/DELETE. Dead tuples consume space until autovacuum reclaims them. VACUUM FULL rewrites the table but locks it."}
        ]
    },

    "Blockchain Developer": {
        "icon": "⛓️",
        "category": "Emerging Tech (Robotics, IoT & Blockchain)",
        "image": str(BASE_ASSETS / "block1.png"),
        "tagline": "Build decentralized applications (dApps), smart contracts, and Web3 consensus protocols.",
        "salary_range": "₹10L – ₹35L LPA (Est. India Market)",
        "salary_details": [
            {"level": "Junior Web3 / Smart Contract Dev", "salary": "₹10L – ₹15L LPA", "exp": "0–2 years"},
            {"level": "Blockchain Developer (2–5 yrs)", "salary": "₹15L – ₹26L LPA", "exp": "2–5 years"},
            {"level": "Lead Blockchain Architect", "salary": "₹26L – ₹45L+ LPA", "exp": "5+ years"}
        ],
        "demand": "Trending",
        "est_time": "6–9 months",
        "readiness_base": 20,
        "readiness_max": 85,
        "skills": [
            {"name": "Solidity Smart Contract Development", "current": 30, "required": 95},
            {"name": "EVM Internals & Gas Optimization", "current": 20, "required": 85},
            {"name": "Hardhat / Foundry Tooling", "current": 30, "required": 90},
            {"name": "Ethers.js / Viem & Web3 Frontend", "current": 40, "required": 85},
            {"name": "Smart Contract Auditing & Security", "current": 15, "required": 80}
        ],
        "phases": [
            {"num": "Phase 1", "name": "Cryptography & Blockchain Basics", "duration": "0 – 4 weeks", "tags": ["Hashing", "Asymmetric Keys", "Consensus (PoS)", "Ethereum Nodes"]},
            {"num": "Phase 2", "name": "Solidity Smart Contracts", "duration": "4 – 10 weeks", "tags": ["Solidity", "ERC-20", "ERC-721", "Hardhat", "Foundry Testing"]},
            {"num": "Phase 3", "name": "Full Stack dApp Development", "duration": "10 – 16 weeks", "tags": ["Wagmi", "Viem", "WalletConnect", "IPFS", "The Graph"]},
            {"num": "Phase 4", "name": "Security & Gas Optimization", "duration": "16 – 22 weeks", "tags": ["Reentrancy Attacks", "Slither", "Gas Optimization", "Layer 2 Rollups"]}
        ],
        "resources": [
            {"name": "CryptoZombies Interactive Solidity Tutorial", "desc": "Step-by-step game building in Solidity", "type": "Interactive", "cost": "Free", "url": "https://cryptozombies.io"},
            {"name": "Ethereum.org Developer Docs", "desc": "The official guides, documentation, and tools for Ethereum", "type": "Documentation", "cost": "Free", "url": "https://ethereum.org/en/developers/"}
        ],
        "projects": [
            {"title": "Decentralized Escrow & Staking Protocol", "difficulty": "Advanced", "tech": ["Solidity", "Foundry", "OpenZeppelin"], "objectives": ["Timelock withdrawal logic", "Yield calculation", "Fuzz testing"]},
            {"title": "Web3 Crowdfunding dApp", "difficulty": "Intermediate", "tech": ["React", "Viem", "Solidity", "IPFS"], "objectives": ["Wallet connection", "Contribution milestones", "Refund guarantee"]}
        ],
        "stages": [
            {"title": "Stage 1: Cryptographic Principles & Consensus", "duration": "4 weeks", "milestones": ["Understand SHA-256, Merkle Trees, and public-private key cryptography", "Differentiate Proof-of-Work and Proof-of-Stake consensus", "Connect to local testnets via JSON-RPC"]},
            {"title": "Stage 2: Solidity Contract Development", "duration": "6 weeks", "milestones": ["Write standard ERC-20 and ERC-721 token contracts", "Manage contract state variables, visibility, and modifiers", "Write unit tests using Foundry and Hardhat"]},
            {"title": "Stage 3: Full Stack dApp Frontend Integration", "duration": "5 weeks", "milestones": ["Connect MetaMask and browser wallets via Wagmi/Viem", "Index on-chain events and query using The Graph subgraphs", "Store decentralized media metadata on IPFS"]},
            {"title": "Stage 4: Security Audits & Gas Optimization", "duration": "5 weeks", "milestones": ["Prevent reentrancy, integer overflow, and front-running exploits", "Optimize storage slot packing to minimize gas consumption", "Run automated static analysis scans with Slither"]}
        ],
        "interview": [
            {"category": "Technical", "q": "What is a Reentrancy attack in Solidity, and how do you protect against it?", "tip": "Explain malicious contracts calling back into a function before state updates complete. Protect using Checks-Effects-Interactions pattern or OpenZeppelin ReentrancyGuard."},
            {"category": "Technical", "q": "How does gas work in Ethereum, and what are storage slot packings?", "tip": "Gas measures computational effort. Storage is read/written in 32-byte slots (20,000 gas for cold write). Packing smaller datatypes (e.g., uint128) into one slot saves gas."}
        ]
    },

    "AR/VR Developer": {
        "icon": "🥽",
        "category": "Emerging Tech (Robotics, IoT & Blockchain)",
        "image": str(BASE_ASSETS / "ar1_p.png"),
        "tagline": "Build immersive 3D spatial simulations, games, and augmented reality applications.",
        "salary_range": "₹8L – ₹25L LPA (Est. India Market)",
        "salary_details": [
            {"level": "Junior AR/VR Developer", "salary": "₹8L – ₹12L LPA", "exp": "0–2 years"},
            {"level": "Mid-Level Spatial Engineer", "salary": "₹12L – ₹19L LPA", "exp": "2–5 years"},
            {"level": "Senior XR Architect", "salary": "₹19L – ₹32L+ LPA", "exp": "5+ years"}
        ],
        "demand": "Growing",
        "est_time": "5–8 months",
        "readiness_base": 25,
        "readiness_max": 88,
        "skills": [
            {"name": "Unity 3D Engine / Unreal Engine", "current": 40, "required": 95},
            {"name": "C# Scripting & 3D Math (Vectors/Quaternions)", "current": 45, "required": 90},
            {"name": "XR Interaction Toolkit & OpenXR", "current": 25, "required": 85},
            {"name": "ARKit / ARCore Mobile Tracking", "current": 30, "required": 80},
            {"name": "3D Asset Optimization & Shaders", "current": 25, "required": 75}
        ],
        "phases": [
            {"num": "Phase 1", "name": "3D Foundations & C#", "duration": "0 – 5 weeks", "tags": ["C#", "Unity UI", "Vectors", "Transforms", "Physics & Colliders"]},
            {"num": "Phase 2", "name": "VR Interactions", "duration": "5 – 10 weeks", "tags": ["OpenXR", "Head Tracking", "Hand Gestures", "Teleportation", "Grab Mechanics"]},
            {"num": "Phase 3", "name": "AR Development", "duration": "10 – 15 weeks", "tags": ["ARCore", "Plane Detection", "Image Tracking", "Light Estimation"]},
            {"num": "Phase 4", "name": "Performance & Spatial Audio", "duration": "15 – 20 weeks", "tags": ["Draw Calls", "Occlusion Culling", "Spatial Audio", "Quest 3 Deploy"]}
        ],
        "resources": [
            {"name": "Unity Learn XR Pathways", "desc": "Official interactive courses for augmented and virtual reality", "type": "Platform", "cost": "Free", "url": "https://learn.unity.com"},
            {"name": "Meta XR Developer Center", "desc": "Guides for Meta Quest and spatial headset development", "type": "Documentation", "cost": "Free", "url": "https://developer.oculus.com"}
        ],
        "projects": [
            {"title": "VR Interactive Physics Laboratory", "difficulty": "Intermediate", "tech": ["Unity", "C#", "OpenXR"], "objectives": ["6-DoF hand tracking", "Gravity simulation", "Haptic feedback"]},
            {"title": "AR Furniture Placement App", "difficulty": "Intermediate", "tech": ["ARCore", "Unity", "C#"], "objectives": ["Horizontal plane detection", "Pinch-to-scale", "Shadow casting"]}
        ],
        "stages": [
            {"title": "Stage 1: 3D Math & Unity C# Architecture", "duration": "5 weeks", "milestones": ["Understand vector operations, dot products, and quaternions", "Build component physics interactions with Rigidbody and Colliders", "Optimize 3D scene hierarchies"]},
            {"title": "Stage 2: VR Headset Interactions with OpenXR", "duration": "5 weeks", "milestones": ["Configure OpenXR input mappings for controllers and hand tracking", "Implement comfortable locomotion and teleportation mechanics", "Integrate realistic haptic feedback triggers"]},
            {"title": "Stage 3: Mobile Augmented Reality with ARFoundation", "duration": "5 weeks", "milestones": ["Detect horizontal and vertical real-world planes with ARCore/ARKit", "Implement raycasting to anchor digital assets in real space", "Estimate lighting temperature for realistic rendering"]},
            {"title": "Stage 4: Framerate Optimization & Spatial Audio", "duration": "5 weeks", "milestones": ["Profile GPU/CPU draw calls to maintain strict 72/90 FPS VR targets", "Configure occlusion culling and LOD (Level of Detail) meshes", "Deploy spatial HRTF 3D audio sources"]}
        ],
        "interview": [
            {"category": "Technical", "q": "Why is maintaining high frame rates (72–90+ FPS) critical in VR development, and what is motion-to-photon latency?", "tip": "Low frame rates or latency over 20ms induce severe vestibular mismatch (simulator sickness). Motion-to-photon is delay from physical head turn to screen photon update."},
            {"category": "Technical", "q": "What is the difference between Quaternions and Euler Angles when handling 3D rotations in Unity?", "tip": "Euler angles suffer from Gimbal Lock (loss of one degree of freedom). Quaternions represent rotations in 4D space, avoiding gimbal lock and enabling smooth interpolation."}
        ]
    },

    "IoT Engineer": {
        "icon": "📡",
        "category": "Emerging Tech (Robotics, IoT & Blockchain)",
        "image": str(BASE_ASSETS / "iot.png"),
        "tagline": "Connect microcontrollers, sensor nodes, and telemetry pipelines to cloud dashboards.",
        "salary_range": "₹6L – ₹22L LPA (Est. India Market)",
        "salary_details": [
            {"level": "Junior IoT Engineer", "salary": "₹6L – ₹9.5L LPA", "exp": "0–2 years"},
            {"level": "Mid-Level IoT Developer", "salary": "₹9.5L – ₹16L LPA", "exp": "2–5 years"},
            {"level": "Senior IoT Solutions Architect", "salary": "₹16L – ₹26L+ LPA", "exp": "5+ years"}
        ],
        "demand": "Growing",
        "est_time": "5–8 months",
        "readiness_base": 30,
        "readiness_max": 88,
        "skills": [
            {"name": "Embedded C / C++ & MicroPython", "current": 45, "required": 90},
            {"name": "Hardware Protocols (I2C, SPI, UART)", "current": 40, "required": 85},
            {"name": "IoT Communication (MQTT, CoAP, HTTP)", "current": 45, "required": 90},
            {"name": "Microcontrollers (ESP32, Raspberry Pi)", "current": 50, "required": 90},
            {"name": "Cloud IoT Hubs (AWS IoT Core, ThingsBoard)", "current": 25, "required": 80}
        ],
        "phases": [
            {"num": "Phase 1", "name": "Embedded Systems Basics", "duration": "0 – 4 weeks", "tags": ["C Programming", "GPIO Pins", "Analog vs Digital", "ESP32", "Sensors"]},
            {"num": "Phase 2", "name": "Hardware Communication Protocols", "duration": "4 – 8 weeks", "tags": ["I2C Bus", "SPI Protocol", "UART Serial", "Interrupts", "Timers"]},
            {"num": "Phase 3", "name": "Network & IoT Protocols", "duration": "8 – 13 weeks", "tags": ["WiFi/BLE", "MQTT Broker", "JSON Payloads", "OTA Updates"]},
            {"num": "Phase 4", "name": "Cloud Integration & Dashboards", "duration": "13 – 18 weeks", "tags": ["AWS IoT Core", "ThingsBoard", "Time-Series DB", "Fleet Management"]}
        ],
        "resources": [
            {"name": "ESP32 Official Espressif Docs", "desc": "Hardware specs, pinouts, and ESP-IDF programming guide", "type": "Documentation", "cost": "Free", "url": "https://docs.espressif.com"},
            {"name": "HiveMQ MQTT Essentials", "desc": "The complete reference series on the MQTT protocol", "type": "Guide", "cost": "Free", "url": "https://www.hivemq.com/mqtt-essentials/"}
        ],
        "projects": [
            {"title": "Smart Environmental Monitor with MQTT", "difficulty": "Intermediate", "tech": ["ESP32", "DHT22", "MQTT", "Python"], "objectives": ["Low-power sleep cycles", "Telemetry publishing", "Live dashboard"]},
            {"title": "Secure Over-The-Air (OTA) Firmware Updater", "difficulty": "Advanced", "tech": ["C++", "HTTPS", "ESP-IDF"], "objectives": ["Cryptographic signature check", "Rollback on failure", "Fleet rollout"]}
        ],
        "stages": [
            {"title": "Stage 1: Embedded Hardware & GPIO Control", "duration": "4 weeks", "milestones": ["Program ESP32 microcontrollers in C++", "Read digital and analog sensor voltages accurately", "Implement hardware timer interrupts"]},
            {"title": "Stage 2: Bus Protocols & Device Interfaces", "duration": "4 weeks", "milestones": ["Interface multiple peripherals on a shared I2C bus", "Transmit high-speed sensor data over SPI", "Debug serial packets with logic analyzers"]},
            {"title": "Stage 3: Wireless Telemetry with MQTT", "duration": "4 weeks", "milestones": ["Connect hardware to local WiFi and Bluetooth Low Energy", "Publish and subscribe to MQTT topics with QoS levels", "Implement deep sleep power management"]},
            {"title": "Stage 4: Cloud Telemetry & Fleet Management", "duration": "4 weeks", "milestones": ["Provision certificates on AWS IoT Core", "Store sensor telemetry in InfluxDB time-series databases", "Deploy secure Over-The-Air (OTA) firmware updates"]}
        ],
        "interview": [
            {"category": "Technical", "q": "Why is MQTT preferred over HTTP for constrained IoT device networks?", "tip": "MQTT is lightweight with 2-byte header overhead vs bulky HTTP headers. It uses persistent TCP sockets, publish/subscribe model, and QoS guarantees for flaky networks."},
            {"category": "Technical", "q": "Explain the difference between I2C and SPI protocols. When would you choose one over the other?", "tip": "I2C uses 2 wires (SDA/SCL) and supports multi-master with device addressing (simpler wiring). SPI uses 4 wires (MOSI/MISO/SCK/CS), is full-duplex, and offers much higher speeds."}
        ]
    },

    "Robotics Engineer": {
        "icon": "🤖",
        "category": "Emerging Tech (Robotics, IoT & Blockchain)",
        "image": str(BASE_ASSETS / "robotics.jpg"),
        "tagline": "Design autonomous robotic systems, kinematic controls, computer vision, and ROS navigation.",
        "salary_range": "₹8L – ₹30L LPA (Est. India Market)",
        "salary_details": [
            {"level": "Junior Robotics Engineer", "salary": "₹8L – ₹12L LPA", "exp": "0–2 years"},
            {"level": "Robotics Software Engineer", "salary": "₹12L – ₹20L LPA", "exp": "2–5 years"},
            {"level": "Senior Robotics Architect / Lead", "salary": "₹20L – ₹36L+ LPA", "exp": "5+ years"}
        ],
        "demand": "Growing",
        "est_time": "6–10 months",
        "readiness_base": 20,
        "readiness_max": 85,
        "skills": [
            {"name": "ROS / ROS 2 (Robot Operating System)", "current": 35, "required": 90},
            {"name": "C++ & Python for Robotics", "current": 50, "required": 90},
            {"name": "Kinematics & Dynamics (URDF)", "current": 30, "required": 85},
            {"name": "SLAM & Autonomous Navigation (Nav2)", "current": 25, "required": 85},
            {"name": "Computer Vision (OpenCV)", "current": 35, "required": 80}
        ],
        "phases": [
            {"num": "Phase 1", "name": "Math & Robotics Fundamentals", "duration": "0 – 5 weeks", "tags": ["Linear Algebra", "Transform Matrices", "C++ Modern", "Linux"]},
            {"num": "Phase 2", "name": "ROS 2 Core", "duration": "5 – 10 weeks", "tags": ["Nodes", "Topics", "Services", "Actions", "URDF Models", "Gazebo Simulation"]},
            {"num": "Phase 3", "name": "Perception & Computer Vision", "duration": "10 – 16 weeks", "tags": ["OpenCV", "Point Cloud Library", "Depth Cameras", "LiDAR Filtering"]},
            {"num": "Phase 4", "name": "SLAM & Autonomous Navigation", "duration": "16 – 24 weeks", "tags": ["Nav2", "Cartographer SLAM", "Costmaps", "Path Planning (A*, DWA)"]}
        ],
        "resources": [
            {"name": "ROS 2 Documentation & Tutorials", "desc": "Official Robot Operating System 2 learning pathway", "type": "Documentation", "cost": "Free", "url": "https://docs.ros.org/en/foxy/"},
            {"name": "The Construct (ROSject)", "desc": "Hands-on browser-based robotics simulation sandboxes", "type": "Platform", "cost": "Free / Paid", "url": "https://www.theconstruct.ai"}
        ],
        "projects": [
            {"title": "Autonomous Indoor Delivery Robot in Gazebo", "difficulty": "Advanced", "tech": ["ROS 2", "Gazebo", "Nav2", "LiDAR"], "objectives": ["URDF mobile base", "Cartographer 2D mapping", "Dynamic obstacle avoidance"]},
            {"title": "Robotic Arm Color-Sorting Vision System", "difficulty": "Intermediate", "tech": ["Python", "OpenCV", "Inverse Kinematics"], "objectives": ["Object centroid detection", "Kinematic angle solve", "Pick-and-place execution"]}
        ],
        "stages": [
            {"title": "Stage 1: Robotics Math & ROS 2 Architecture", "duration": "5 weeks", "milestones": ["Understand rotation matrices and homogenous transformations", "Write ROS 2 publisher/subscriber nodes in C++ and Python", "Model multi-link robot geometries using URDF/Xacro"]},
            {"title": "Stage 2: Physics Simulation in Gazebo", "duration": "5 weeks", "milestones": ["Simulate differential drive robots inside Gazebo environments", "Attach virtual sensors (2D LiDAR, Depth Cameras, IMU)", "Broadcast coordinate frames using tf2 transforms"]},
            {"title": "Stage 3: Sensor Fusion & Perception Pipelines", "duration": "5 weeks", "milestones": ["Process 2D LiDAR scans and filter point clouds", "Detect objects and calculate coordinates via OpenCV", "Fuse wheel odometry and IMU data using Extended Kalman Filters"]},
            {"title": "Stage 4: Simultaneous Localization & Mapping (SLAM)", "duration": "5 weeks", "milestones": ["Build 2D occupancy grid maps with Cartographer/Slam-Toolbox", "Configure Nav2 global and local costmap layers", "Execute autonomous path planning with obstacle recovery"]}
        ],
        "interview": [
            {"category": "Technical", "q": "What is SLAM (Simultaneous Localization and Mapping), and why is it challenging?", "tip": "The robot needs a map to know where it is, and needs to know where it is to build a map. It solves this chicken-and-egg problem by fusing odometry, LiDAR, and loop closure."},
            {"category": "Technical", "q": "Explain Forward Kinematics vs Inverse Kinematics for a robotic manipulator arm.", "tip": "Forward Kinematics calculates end-effector spatial position from known joint angles (direct). Inverse Kinematics solves for required joint angles to reach a target coordinate (often nonlinear with multiple solutions)."}
        ]
    },

    "Digital Marketing Specialist": {
        "icon": "📢",
        "category": "Digital Marketing & SEO",
        "image": str(BASE_ASSETS / "digital.png"),
        "tagline": "Drive customer acquisition, scale paid media funnels, and optimize conversion rates.",
        "salary_range": "₹4L – ₹15L LPA (Est. India Market)",
        "salary_details": [
            {"level": "Junior Marketing Executive", "salary": "₹4L – ₹6L LPA", "exp": "0–2 years"},
            {"level": "Digital Marketing Specialist", "salary": "₹6L – ₹11L LPA", "exp": "2–4 years"},
            {"level": "Growth Marketing Lead", "salary": "₹11L – ₹20L+ LPA", "exp": "4+ years"}
        ],
        "demand": "High Demand",
        "est_time": "3–4 months",
        "readiness_base": 55,
        "readiness_max": 95,
        "skills": [
            {"name": "Performance Marketing (Meta Ads / Google Ads)", "current": 60, "required": 95},
            {"name": "Web Analytics (Google Analytics 4 / Tag Manager)", "current": 50, "required": 90},
            {"name": "Conversion Rate Optimization (CRO)", "current": 40, "required": 85},
            {"name": "Email Marketing & Retention (Klaviyo/Mailchimp)", "current": 55, "required": 85},
            {"name": "Content Strategy & Copywriting", "current": 65, "required": 90}
        ],
        "phases": [
            {"num": "Phase 1", "name": "Marketing Foundations & GA4", "duration": "0 – 3 weeks", "tags": ["Funnel Strategy", "GA4 Event Tracking", "Google Tag Manager", "UTM Tracking"]},
            {"num": "Phase 2", "name": "Paid Search & Display (Google Ads)", "duration": "3 – 6 weeks", "tags": ["Search Ads", "Quality Score", "Keyword Bidding", "PMax Campaigns"]},
            {"num": "Phase 3", "name": "Paid Social & Creative Funnels", "duration": "6 – 10 weeks", "tags": ["Meta Ads Manager", "Audience Pixel", "CBO Bidding", "Creative Testing"]},
            {"num": "Phase 4", "name": "Retention & CRO", "duration": "10 – 14 weeks", "tags": ["Email Automation", "Landing Page A/B Testing", "LTV:CAC Ratios"]}
        ],
        "resources": [
            {"name": "Google Skillshop", "desc": "Official free certifications for Google Ads and Analytics", "type": "Platform", "cost": "Free", "url": "https://skillshop.withgoogle.com"},
            {"name": "HubSpot Academy", "desc": "Free inbound marketing, email, and social media certifications", "type": "Platform", "cost": "Free", "url": "https://academy.hubspot.com"}
        ],
        "projects": [
            {"title": "Multi-Channel Paid Ads Growth Campaign", "difficulty": "Intermediate", "tech": ["Google Ads", "Meta Ads", "GA4"], "objectives": ["Target CAC below ₹800", "A/B ad creative variations", "ROAS tracking"]},
            {"title": "E-Commerce Automated Retention Email Flow", "difficulty": "Beginner", "tech": ["Klaviyo", "Figma"], "objectives": ["Abandoned cart sequence", "Post-purchase cross-sell", "Dynamic discounts"]}
        ],
        "stages": [
            {"title": "Stage 1: Analytics Tagging & Event Tracking", "duration": "3 weeks", "milestones": ["Configure Google Tag Manager web triggers", "Implement Google Analytics 4 conversion purchase events", "Audit UTM tracking parameters across marketing channels"]},
            {"title": "Stage 2: Paid Search Acquisition on Google", "duration": "3 weeks", "milestones": ["Conduct keyword commercial intent research", "Optimize Google Search Ad Quality Scores", "Structure Performance Max campaigns"]},
            {"title": "Stage 3: Paid Social Funnels on Meta", "duration": "3 weeks", "milestones": ["Configure Meta Conversions API (CAPI) for privacy tracking", "Build top-of-funnel Lookalike and retargeting custom audiences", "Analyze creative hook rates and click-through rates"]},
            {"title": "Stage 4: Conversion Rate Optimization & Retention", "duration": "3 weeks", "milestones": ["Design landing page A/B tests to optimize conversion rates", "Build automated email win-back and abandonment drip flows", "Calculate Customer Lifetime Value (LTV) to CAC ratios"]}
        ],
        "interview": [
            {"category": "Case", "q": "Your Meta Ads campaign has a high Click-Through Rate (4%) but an extremely low conversion rate (0.4%). What is wrong and how do you fix it?", "tip": "Analyze disconnect between ad hook and landing page promise, check page loading speed, evaluate checkout friction, pricing resistance, or audience targeting misalignment."},
            {"category": "Technical", "q": "What is the difference between ROAS and ROI in digital marketing?", "tip": "ROAS (Return on Ad Spend) measures gross revenue generated per ad dollar. ROI factors in all operational expenses (product COGS, shipping, agency fees) for true net profit."}
        ]
    },

    "SEO Specialist": {
        "icon": "🔍",
        "category": "Digital Marketing & SEO",
        "image": str(BASE_ASSETS / "seo.png"),
        "tagline": "Optimize organic search rankings, execute technical site audits, and drive compounding traffic.",
        "salary_range": "₹4L – ₹12L LPA (Est. India Market)",
        "salary_details": [
            {"level": "Junior SEO Analyst (0–2 yrs)", "salary": "₹4L – ₹6L LPA", "exp": "0–2 years"},
            {"level": "SEO Specialist (2–4 yrs)", "salary": "₹6L – ₹10L LPA", "exp": "2–4 years"},
            {"level": "Head of Organic Growth (4+ yrs)", "salary": "₹10L – ₹18L+ LPA", "exp": "4+ years"}
        ],
        "demand": "Stable",
        "est_time": "3–5 months",
        "readiness_base": 50,
        "readiness_max": 92,
        "skills": [
            {"name": "Technical SEO & Crawl Budget (Screaming Frog)", "current": 50, "required": 95},
            {"name": "Keyword Research & Content Clustering", "current": 65, "required": 90},
            {"name": "On-Page Optimization & Schema Markup", "current": 60, "required": 90},
            {"name": "Link Building & Digital PR", "current": 40, "required": 80},
            {"name": "Google Search Console & GA4", "current": 60, "required": 90}
        ],
        "phases": [
            {"num": "Phase 1", "name": "Search Engine Fundamentals", "duration": "0 – 3 weeks", "tags": ["Crawling", "Indexing", "Ranking", "Search Intent", "Google Search Console"]},
            {"num": "Phase 2", "name": "On-Page SEO & Content Strategy", "duration": "3 – 7 weeks", "tags": ["Keyword Research", "Topic Clusters", "Title/Meta Tags", "Schema.org"]},
            {"num": "Phase 3", "name": "Technical SEO Audits", "duration": "7 – 11 weeks", "tags": ["Screaming Frog", "Core Web Vitals", "Canonical Tags", "Robots.txt", "Sitemaps"]},
            {"num": "Phase 4", "name": "Off-Page SEO & Performance Growth", "duration": "11 – 15 weeks", "tags": ["Backlinks", "Domain Authority", "Digital PR", "Competitor Gap Analysis"]}
        ],
        "resources": [
            {"name": "Google Search Central Documentation", "desc": "Official search quality guidelines and technical documentation", "type": "Documentation", "cost": "Free", "url": "https://developers.google.com/search"},
            {"name": "Ahrefs SEO Academy", "desc": "Free actionable video courses on keyword research and link building", "type": "Course", "cost": "Free", "url": "https://ahrefs.com/academy"}
        ],
        "projects": [
            {"title": "Full Website Technical SEO Audit & Remediation", "difficulty": "Intermediate", "tech": ["Screaming Frog", "Google Search Console"], "objectives": ["Identify 404 & 301 redirect chains", "Fix duplicate canonicals", "Audit Core Web Vitals"]},
            {"title": "Programmatic SEO Keyword Clustering Strategy", "difficulty": "Intermediate", "tech": ["Python", "Ahrefs", "Google Sheets"], "objectives": ["Cluster 1,000 search queries", "Map intent pillars", "Content brief templates"]}
        ],
        "stages": [
            {"title": "Stage 1: Search Architecture & Search Console", "duration": "3 weeks", "milestones": ["Verify sites and monitor index coverage in Google Search Console", "Dissect canonicalization rules and noindex directives", "Configure XML sitemaps and robots.txt rules"]},
            {"title": "Stage 2: Keyword Intent & Semantic Content Clusters", "duration": "4 weeks", "milestones": ["Conduct keyword search volume and difficulty research", "Group search keywords into hub-and-spoke topic clusters", "Implement Schema.org structured data (Article, FAQ, Product)"]},
            {"title": "Stage 3: Technical Site Crawling & Speed Optimization", "duration": "4 weeks", "milestones": ["Perform site crawls with Screaming Frog to identify indexation blockers", "Diagnose Core Web Vitals (LCP, CLS, INP) issues", "Resolve duplicate content and hreflang multilingual issues"]},
            {"title": "Stage 4: Authoritative Link Building & Performance Tracking", "duration": "3 weeks", "milestones": ["Execute high-authority editorial backlink acquisition", "Analyze organic keyword ranking movements in SERPs", "Prepare monthly executive traffic growth ROI decks"]}
        ],
        "interview": [
            {"category": "Technical", "q": "What is the difference between a 301 and a 302 redirect from an SEO standpoint?", "tip": "A 301 is a permanent redirect that passes ~99% of link equity (PageRank). A 302 is temporary, so search engines retain the original URL in the index without passing equity."},
            {"category": "Technical", "q": "What are Canonical tags (rel='canonical'), and when should you use them?", "tip": "Canonical tags tell search engines which URL represents the master copy when duplicate or near-identical content exists (e.g., product pages with different color filter query parameters)."}
        ]
    },

    "Mobile App Developer": {
        "icon": "📱",
        "category": "Web Development",
        "image": str(BASE_ASSETS / "mobile.png"),
        "tagline": "Build cross-platform iOS and Android mobile apps using React Native or Flutter.",
        "salary_range": "₹5L – ₹18L LPA (Est. India Market)",
        "salary_details": [
            {"level": "Junior Mobile App Developer", "salary": "₹5L – ₹8.5L LPA", "exp": "0–2 years"},
            {"level": "Mid-Level Mobile Developer", "salary": "₹8.5L – ₹15L LPA", "exp": "2–5 years"},
            {"level": "Senior Lead Mobile Architect", "salary": "₹15L – ₹28L+ LPA", "exp": "5+ years"}
        ],
        "demand": "High Demand",
        "est_time": "4–6 months",
        "readiness_base": 40,
        "readiness_max": 92,
        "skills": [
            {"name": "React Native or Flutter (Dart)", "current": 50, "required": 90},
            {"name": "State Management (Redux/Bloc/Zustand)", "current": 45, "required": 85},
            {"name": "Native Device APIs (Camera, GPS, Bluetooth)", "current": 35, "required": 85},
            {"name": "Offline Caching & Local Storage (SQLite/Watermelon)", "current": 35, "required": 80},
            {"name": "App Store & Play Store Deployment", "current": 30, "required": 75}
        ],
        "phases": [
            {"num": "Phase 1", "name": "Language & Mobile Basics", "duration": "0 – 4 weeks", "tags": ["React Native / Flutter", "Flexbox Mobile", "Touch Gestures", "Navigation"]},
            {"num": "Phase 2", "name": "Native Hardware APIs & State", "duration": "4 – 8 weeks", "tags": ["AsyncStorage / SQLite", "Camera API", "Geolocation", "Push Notifications"]},
            {"num": "Phase 3", "name": "Offline Sync & Performance", "duration": "8 – 13 weeks", "tags": ["Offline First", "Fastlane", "Optimistic Updates", "Memory Profiling"]},
            {"num": "Phase 4", "name": "App Store Publishing", "duration": "13 – 18 weeks", "tags": ["App Store Connect", "Google Play Console", "CodePush", "Crashlytics"]}
        ],
        "resources": [
            {"name": "React Native Official Docs", "desc": "Interactive guides for cross-platform native development", "type": "Documentation", "cost": "Free", "url": "https://reactnative.dev"},
            {"name": "Flutter Official Documentation", "desc": "Complete widget references and Dart language guides", "type": "Documentation", "cost": "Free", "url": "https://flutter.dev"}
        ],
        "projects": [
            {"title": "Offline-First Fitness & Calorie Tracker App", "difficulty": "Intermediate", "tech": ["React Native", "SQLite", "Victory Native"], "objectives": ["Offline persistence", "Progress charts", "Step count sensor"]},
            {"title": "Real-Time Food Delivery App Interface", "difficulty": "Intermediate", "tech": ["Flutter", "Google Maps SDK", "WebSockets"], "objectives": ["Live driver courier pin", "Order status tracking", "Payment integration"]}
        ],
        "stages": [
            {"title": "Stage 1: Mobile UI Architecture & Touch Navigation", "duration": "4 weeks", "milestones": ["Build smooth mobile interfaces with React Native / Flutter", "Implement stack and bottom-tab navigation", "Handle touch gestures and keyboard avoid views"]},
            {"title": "Stage 2: Native Device Integrations", "duration": "4 weeks", "milestones": ["Access native hardware APIs (Camera, GPS Location, Gyroscope)", "Request and handle user system permissions cleanly", "Configure push notifications via Firebase Cloud Messaging"]},
            {"title": "Stage 3: Offline-First Architecture & Caching", "duration": "5 weeks", "milestones": ["Store structured local data with SQLite / WatermelonDB", "Synchronize offline queued mutations when connection resumes", "Profile render FPS and optimize memory allocations"]},
            {"title": "Stage 4: Automated Build & Store Publishing", "duration": "4 weeks", "milestones": ["Automate release builds using Fastlane", "Configure code signing certificates for iOS and Android", "Publish apps on the Google Play Store and Apple App Store"]}
        ],
        "interview": [
            {"category": "Technical", "q": "How does the React Native Bridge work, and how does the New Architecture (JSI / Fabric) improve performance?", "tip": "Legacy architecture serialized JSON messages asynchronously over a C++ bridge. The New Architecture uses JSI (JavaScript Interface) for direct synchronous C++ memory calls, eliminating serialization bottlenecks."},
            {"category": "Technical", "q": "How do you handle background tasks and offline data synchronization in mobile applications?", "tip": "Use background fetch jobs, local SQLite queues for pending mutations, network state listeners, and optimistic UI updates to ensure a seamless user experience."}
        ]
    }
}

# Add helper metadata for filtering and navigation
CAREER_CATEGORIES = [
    "All Categories",
    "Web Development",
    "AI & Machine Learning",
    "Data Science & Analytics",
    "Cloud & DevOps",
    "Cybersecurity",
    "UI / UX Design",
    "Management & Delivery",
    "Quality Assurance & Testing",
    "Database Administration",
    "Emerging Tech (Robotics, IoT & Blockchain)",
    "Digital Marketing & SEO"
]

SALARY_FILTERS = [
    "All Salary Ranges",
    "₹4L+ LPA",
    "₹6L+ LPA",
    "₹8L+ LPA",
    "₹10L+ LPA"
]

DEMAND_FILTERS = [
    "All Demand Levels",
    "Top Demand",
    "Very High",
    "High Demand",
    "Trending",
    "Growing",
    "Stable"
]
