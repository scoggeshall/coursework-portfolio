/* =========================================================================
   Sean Coggeshall — Coursework Portfolio
   Renders the live-demo index and the course catalog, handles filtering,
   and remembers the theme choice.
   ========================================================================= */

/* -------------------------------------------------------------------------
   Set this once the repo is on GitHub, e.g.
       "https://github.com/<user>/<repo>/blob/main/"
   Every "View source" link then points at the file on GitHub instead of the
   raw file next to this page. Leave it as "" to keep links relative.
   ------------------------------------------------------------------------- */
const REPO_BASE = "";

/* ------------------------------------------------------------------ demos */

const DEMOS = [
    {
        name: "The Evolution Of Video Games",
        course: "WEBD221",
        note: "Four-page site — overview, console wars, favourites, and a validated submission form.",
        url: "Intermediate-Web-Development-WEBD221/Assignments/WK7_Assignment/index.html"
    },
    {
        name: "JavaScript Final Project",
        course: "WEBD241",
        note: "Seven assignments collected behind a jQuery drop-down menu.",
        url: "WebDev-Using-JavaScript-WEBD241/FinalProject/FinalProject.html"
    },
    {
        name: "jQuery Interaction Set",
        course: "WEBD343",
        note: "Jacksonville beaches accordion, built as a reusable jQuery plugin.",
        url: "jQuery-WEBD343/Assignments/WK8/index.html"
    },
    {
        name: "User Interface Design",
        course: "WEBD300",
        note: "Coggs Web Craft landing page plus nine responsive template variants.",
        url: "User-Interface-Design-WEBD300/index.html"
    },
    {
        name: "Information Security Analyst",
        course: "Web Development Fundamentals",
        note: "Three-page career site — the Associate's final web project.",
        url: "Web-Development-Fundamentals/Final%20Project/index.html"
    },
    {
        name: "Ye Music Notes",
        course: "Web Development Fundamentals",
        note: "Five pages covering navigation, tables, forms, and multimedia.",
        url: "Web-Development-Fundamentals/Yesite/index.html"
    }
];

/* ----------------------------------------------------------------- courses
   NOTE: a handful of the Associate's courses were filed on disk by course
   code only, so the code is used as the card title. If you have the official
   titles from the degree plan, drop them into `title` here — nothing else
   needs to change.
   ------------------------------------------------------------------------- */

const COURSES = [
    /* ----- Associate's ----- */
    {
        code: "ENTD200", title: "Fundamentals Of Programming", level: "as",
        areas: ["programming"],
        blurb: "Console applications with real problem domains: a car trip tracker, MPG calculators, and a payroll program with validated numeric input.",
        tags: ["Python", "Functions", "Dictionaries", "Reports"],
        src: "Fundamentals-of-Programming",
        writeups: { slug: "fundamentals", count: 2 }
    },
    {
        code: "WEBD121", title: "Web Development Fundamentals", level: "as",
        areas: ["web"],
        blurb: "HTML and CSS from the ground up — navigation, tables, forms, multimedia, and a first pass at JavaScript, ending in a three-page career site.",
        tags: ["HTML", "CSS", "Forms", "Multimedia"],
        src: "Web-Development-Fundamentals",
        demo: "Web-Development-Fundamentals/Final%20Project/index.html"
    },
    {
        code: "ITCC121", title: "Introduction To Computer Science", level: "as",
        areas: ["systems"],
        blurb: "Computing foundations: a software evaluation paper, a step-by-step PC setup guide, a database presentation, and SDLC waterfall work.",
        tags: ["Hardware", "SDLC", "Databases"],
        src: "ITCC121"
    },
    {
        code: "ITCC231", title: "Introduction To Information Technology Writing", level: "as",
        areas: ["professional"],
        blurb: "Technical writing in APA form — outline, rough draft, midterm project, and a final paper, with weekly discussion work.",
        tags: ["APA", "Technical Writing", "Research"],
        src: "Information-Technology-Writing-ITCC231"
    },
    {
        code: "ITCC298", title: "Computer Technology Intermediate Capstone", level: "as",
        areas: ["systems"],
        blurb: "Associate's capstone: hardware requirements, a user manual, a presentation, a costing spreadsheet, and a final report.",
        tags: ["Requirements", "Documentation", "Capstone"],
        src: "ITCC298"
    },
    {
        code: "ITCC112", title: "Advanced Productivity Applications", level: "as",
        areas: ["data", "professional"],
        blurb: "Applied Excel — formatting, filtering, sorting, multi-sheet workbooks, freezing and views, page layout — with three graded workbook projects.",
        tags: ["Excel", "Filtering", "Workbooks"],
        src: "Advanced-Productivity-Applications"
    },
    {
        code: "ITMG221", title: "IT Project Management", level: "as",
        areas: ["systems", "professional"],
        blurb: "IT management through weekly case-study essays and structured review questions across eight weeks.",
        tags: ["Case Studies", "IT Management"],
        src: "ITMG221"
    },
    {
        code: "", title: "Human Relations", level: "as",
        areas: ["professional"],
        blurb: "Interpersonal communication — a non-verbal communication essay, presentation preparation, and a final paper.",
        tags: ["Communication", "Presentation"],
        src: "Human-Relations"
    },
    {
        code: "STEM185", title: "The History And Context Of STEM", level: "as",
        areas: ["professional"],
        blurb: "Guided essay sequence with structured peer review, a timeline project, and a recorded video walkthrough.",
        tags: ["Peer Review", "Essays"],
        src: "STEM185"
    },
    {
        code: "STEM270", title: "Thinking And Acting Ethically", level: "as",
        areas: ["professional"],
        blurb: "Applied ethics for technology: repeated case-study analyses and a code-of-ethics worksheet.",
        tags: ["Ethics", "Case Analysis"],
        src: "STEM270"
    },

    /* ----- Bachelor's ----- */
    {
        code: "ENTD220", title: "Introduction To Python®", level: "bs",
        areas: ["programming"],
        blurb: "The calculator rebuilt properly: dedicated functions, try/except handling, an imported Mylib module, a menu system, and finally classes with inheritance.",
        tags: ["Python", "Modules", "OOP", "Exceptions"],
        src: "Intro-to-Python/ENTD220"
    },
    {
        code: "ENTD268", title: "Information System Design", level: "bs",
        areas: ["systems"],
        blurb: "Full analysis-and-design document set for one system — SRS with use cases, context and level-0 DFDs, UML, ERD, architecture, structure chart, and an SDD with test cases.",
        tags: ["SRS", "SDD", "DFD", "UML", "ERD"],
        src: "Information-Systems-Design-ENTD268"
    },
    {
        code: "ENTD120", title: "User Experience I", level: "bs",
        areas: ["web", "systems"],
        blurb: "UX research and design: an annotated bibliography, cognitive-mapping work, wireframes, and a final project paper.",
        tags: ["UX", "Wireframes", "Research"],
        src: "User-Experience-ENTD120"
    },
    {
        code: "WEBD221", title: "Intermediate Web Development", level: "bs",
        areas: ["web"],
        blurb: "A multi-page site grown a week at a time — semantic markup, stylesheets, imagery, JavaScript behaviour, and a validated form. Every week kept as its own snapshot.",
        tags: ["HTML5", "CSS", "JavaScript", "Forms"],
        src: "Intermediate-Web-Development-WEBD221",
        demo: "Intermediate-Web-Development-WEBD221/Assignments/WK7_Assignment/index.html"
    },
    {
        code: "ISSC297", title: "Securing Applications", level: "bs",
        areas: ["security"],
        blurb: "Ten hands-on application-security labs plus four case studies, worked against the OWASP testing guide and the CWE/SANS Top 25.",
        tags: ["OWASP", "AppSec", "Labs"],
        src: "Securing-Applications-ISSC297"
    },
    {
        code: "STEM470", title: "Cybersecurity, Surveillance, Privacy And Ethics", level: "bs",
        areas: ["security", "professional"],
        blurb: "Eight weeks on surveillance and privacy — facial recognition, predictive analytics, digital authoritarianism — ending in a case-study profile.",
        tags: ["Privacy", "Surveillance", "Ethics"],
        src: "Cybersecurity-Surveillance-Privacy-and-Ethics-STEM470"
    },
    {
        code: "HRMT101", title: "Human Relations Communication", level: "bs",
        areas: ["professional"],
        blurb: "Communication styles, change management, and global virtual teams, closing with a presentation.",
        tags: ["Communication", "Teams"],
        src: "Human-Relations-Communication-HRMT101",
        writeups: { slug: "hrmt101", count: 3 }
    },
    {
        code: "WEBD122", title: "Introduction To Web Analytics", level: "bs",
        areas: ["data", "web"],
        blurb: "Web data analysis — metrics selection, competitive intelligence, site critique methodology — delivered as weekly reports and two presentations.",
        tags: ["Analytics", "Metrics", "Reporting"],
        src: "Intro-to-Web-Analytics-WEBD122"
    },
    {
        code: "ISSC290", title: "Securing Databases", level: "bs",
        areas: ["security", "databases"],
        blurb: "Eight assignments on database hardening and access control, plus a researched paper taken from outline through draft to final.",
        tags: ["Database Security", "Access Control"],
        src: "Securing-Databases-ISSC290"
    },
    {
        code: "ENTD320", title: "Intermediate Python® Programming", level: "bs",
        areas: ["programming", "web", "databases"],
        blurb: "Flask from a hello-world route to two cooperating microservices over a shared SQLite database — with Jinja2 templates, a history page, and a unittest suite.",
        tags: ["Flask", "Jinja2", "REST", "SQLite", "unittest"],
        src: "Intermediate-Python-Programming-ENTD320",
        writeups: { slug: "entd320", count: 1 }
    },
    {
        code: "INFO400", title: "MongoDB® And Python®", level: "bs",
        areas: ["data", "databases"],
        blurb: "The widest course in the degree: pandas and NumPy, REST and MongoDB, Cartopy mapping, Shapely geospatial dispatch, Apriori association rules, and scikit-learn — then a housing-price regression final.",
        tags: ["pandas", "MongoDB", "scikit-learn", "Apriori", "Geospatial"],
        src: "MongoDB-and-Python-INFO400",
        writeups: { slug: "info400", count: 8 }
    },
    {
        code: "INFO222", title: "Database Concepts", level: "bs",
        areas: ["databases"],
        blurb: "Relational fundamentals worked in SQLite against a medical-records schema, with seven assignments and a walkthrough of the build.",
        tags: ["SQL", "SQLite", "Schema Design"],
        src: "Database-Concepts-INFO222"
    },
    {
        code: "ISSC221", title: "Intermediate Computer Systems", level: "bs",
        areas: ["systems"],
        blurb: "Twelve chapter write-ups on computer systems and architecture, consolidated into a final project.",
        tags: ["Systems", "Architecture"],
        src: "Intermediate-Computer-Systems-ISSC221"
    },
    {
        code: "INFO331", title: "Management Information Systems", level: "bs",
        areas: ["systems", "professional"],
        blurb: "Information systems in a business context, delivered as two recorded presentations with supporting written analysis.",
        tags: ["MIS", "Presentations"],
        src: "Management-Information-Systems-INFO331"
    },
    {
        code: "STEM380", title: "Coevolution Of Society, Culture, And Technology", level: "bs",
        areas: ["professional"],
        blurb: "Two researched papers and a final essay on how technology and society shape one another.",
        tags: ["Research", "Technology & Society"],
        src: "Coevolution-of-Society-Culture-and-Tech-STEM380",
        writeups: { slug: "stem380", count: 5 }
    },
    {
        code: "WEBD300", title: "User Interface Design", level: "bs",
        areas: ["web"],
        blurb: "A template family — default, blog, and portfolio — delivered three times over with dedicated desktop, tablet, and mobile stylesheets.",
        tags: ["UI Design", "Responsive", "Templates"],
        src: "User-Interface-Design-WEBD300",
        demo: "User-Interface-Design-WEBD300/index.html"
    },
    {
        code: "WEBD241", title: "Web Development Using JavaScript®", level: "bs",
        areas: ["web", "programming"],
        blurb: "Seven JavaScript assignments — arrays and sorting, image galleries, form validation — collected behind a jQuery menu in the final project.",
        tags: ["JavaScript", "DOM", "Validation", "jQuery"],
        src: "WebDev-Using-JavaScript-WEBD241",
        demo: "WebDev-Using-JavaScript-WEBD241/FinalProject/FinalProject.html"
    },
    {
        code: "WEBD343", title: "jQuery", level: "bs",
        areas: ["web"],
        blurb: "Four runnable jQuery builds ending in a reusable accordion plugin — selectors and events, an accordion, an image slider, then the plugin rewrite.",
        tags: ["jQuery", "Plugins", "Animation"],
        src: "jQuery-WEBD343",
        demo: "jQuery-WEBD343/Assignments/WK8/index.html"
    },
    {
        code: "INFO498", title: "Information Technology: Capstone", level: "bs",
        areas: ["systems"],
        blurb: "A point-of-sale system specified end to end — network topology, screen layout, project schedule, and a costed build.",
        tags: ["Capstone", "Network Design", "Planning", "Costing"],
        src: "Information-Technology-Capstone-INFO498"
    }
];

const FILTERS = [
    { id: "all", label: "All" },
    { id: "programming", label: "Programming" },
    { id: "web", label: "Web" },
    { id: "data", label: "Data & Analysis" },
    { id: "databases", label: "Databases" },
    { id: "security", label: "Security" },
    { id: "systems", label: "Systems & Design" },
    { id: "professional", label: "Writing & Ethics" },
    { id: "demo", label: "Live Demo" }
];

/* ------------------------------------------------------------------ utils */

const el = (tag, cls, text) => {
    const node = document.createElement(tag);
    if (cls) node.className = cls;
    if (text !== undefined) node.textContent = text;
    return node;
};

const sourceHref = (path) => (REPO_BASE ? REPO_BASE + path : path);

/* ------------------------------------------------------------ demo index */

function renderDemos() {
    const grid = document.querySelector("[data-demo-grid]");
    if (!grid) return;

    DEMOS.forEach((demo) => {
        const card = el("a", "demo");
        card.href = demo.url;
        card.target = "_blank";
        card.rel = "noopener";
        card.appendChild(el("strong", null, demo.name));
        card.appendChild(el("span", null, demo.note));
        card.appendChild(el("em", null, demo.course));
        grid.appendChild(card);
    });
}

/* ------------------------------------------------------------ course grid */

function courseCard(course) {
    const card = el("article", "course" + (course.demo ? " has-demo" : ""));
    card.dataset.areas = course.areas.join(" ") + (course.demo ? " demo" : "");

    const top = el("div", "course-top");
    const lvl = el("span", "lvl " + course.level, course.level === "bs" ? "B.S." : "A.S.");
    top.appendChild(lvl);
    /* Several Associate's courses were filed without a course number, and none
       is recoverable from the syllabi — those cards show the name alone. */
    if (course.code) top.appendChild(el("span", "code", course.code));
    card.appendChild(top);

    card.appendChild(el("h3", null, course.title));
    card.appendChild(el("p", null, course.blurb));

    const tags = el("ul", "tags");
    course.tags.forEach((t) => tags.appendChild(el("li", null, t)));
    card.appendChild(tags);

    const actions = el("div", "actions");
    if (course.demo) {
        const live = el("a", "link-btn live", "Open demo");
        live.href = course.demo;
        live.target = "_blank";
        live.rel = "noopener";
        actions.appendChild(live);
    }
    if (course.writeups) {
        const docs = el("a", "link-btn", `Write-Ups (${course.writeups.count})`);
        docs.href = `writeups/index.html#${course.writeups.slug}`;
        actions.appendChild(docs);
    }
    const src = el("a", "link-btn", "Files");
    src.href = sourceHref(course.src);
    actions.appendChild(src);
    card.appendChild(actions);

    return card;
}

function renderCourses() {
    const grid = document.querySelector("[data-course-grid]");
    const filterBar = document.querySelector("[data-filters]");
    const count = document.querySelector("[data-count]");
    if (!grid || !filterBar) return;

    COURSES.forEach((c) => grid.appendChild(courseCard(c)));

    const cards = Array.from(grid.children);

    const apply = (id) => {
        let shown = 0;
        cards.forEach((card) => {
            const match = id === "all" || card.dataset.areas.split(" ").includes(id);
            card.hidden = !match;
            if (match) shown += 1;
        });
        if (count) {
            count.textContent =
                shown === COURSES.length
                    ? `${COURSES.length} courses · 2 degrees`
                    : `${shown} of ${COURSES.length} courses`;
        }
    };

    FILTERS.forEach((f) => {
        const btn = el("button", "filter", f.label);
        btn.type = "button";
        btn.dataset.filter = f.id;
        btn.setAttribute("aria-pressed", String(f.id === "all"));
        btn.addEventListener("click", () => {
            filterBar.querySelectorAll(".filter").forEach((b) =>
                b.setAttribute("aria-pressed", String(b === btn))
            );
            apply(f.id);
        });
        filterBar.appendChild(btn);
    });

    apply("all");
}

/* ------------------------------------------------- source links + theme */

function wireSourceLinks() {
    document.querySelectorAll("[data-src]").forEach((link) => {
        link.href = sourceHref(link.dataset.src);
    });
}

function wireTheme() {
    const root = document.documentElement;
    const toggle = document.querySelector("[data-theme-toggle]");

    let stored = null;
    try {
        stored = localStorage.getItem("portfolio-theme");
    } catch (e) {
        /* private mode or blocked storage — fall back to the default theme */
    }
    if (stored === "light" || stored === "dark") root.dataset.theme = stored;

    if (!toggle) return;
    toggle.addEventListener("click", () => {
        /* Light is the default, so an unset attribute means light. */
        const next = (root.dataset.theme || "light") === "light" ? "dark" : "light";
        root.dataset.theme = next;
        try {
            localStorage.setItem("portfolio-theme", next);
        } catch (e) {
            /* not persisting is fine; the toggle still works for this visit */
        }
    });
}

/* -------------------------------------------------------------------- go */

renderDemos();
renderCourses();
wireSourceLinks();
wireTheme();

/* The browser resolves a #hash before these sections have been rendered, so a
   direct link like /#coursework lands short. Re-apply it once they exist. */
if (window.location.hash) {
    const target = document.querySelector(window.location.hash);
    if (target) target.scrollIntoView();
}
