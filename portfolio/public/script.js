const PROJECTS = [{"id": "info400", "title": "Florida housing analysis", "subtitle": "Turning monthly housing data into an inspectable regression workflow.", "image": "assets/housing-pipeline.svg", "codes": ["INFO400"]}, {"id": "entd320", "title": "Flask calculator microservices", "subtitle": "Two HTTP services, a shared history, and a browser interface.", "image": "assets/flask-architecture.svg", "codes": ["ENTD320"]}, {"id": "systems", "title": "From requirements to system design", "subtitle": "Data flows, application architecture, and a point-of-sale capstone.", "image": "assets/ContextDFD.png", "codes": ["ENTD268", "INFO498"]}, {"id": "webd300", "title": "Responsive interface design", "subtitle": "A working site and templates for desktop, tablet, and mobile.", "image": "assets/ui-design-demo.png", "codes": ["WEBD300"]}];
const DEMOS = [{"code": "WEBD221", "course": "WEBD221 — Intermediate Web Development", "name": "The Evolution of Video Games", "note": "Four-page site — overview, console wars, favourites, and a validated submission form.", "url": "demos/webd221-evolution-of-video-games/index.html"}, {"code": "WEBD241", "course": "WEBD241 — Web Development Using JavaScript®", "name": "JavaScript Final Project", "note": "Seven assignments collected behind a jQuery drop-down menu.", "url": "demos/webd241-javascript-final/FinalProject.html"}, {"code": "WEBD343", "course": "WEBD343 — jQuery", "name": "jQuery Interaction Set", "note": "Jacksonville beaches accordion, built as a reusable jQuery plugin.", "url": "demos/webd343-jquery/index.html"}, {"code": "WEBD300", "course": "WEBD300 — User Interface Design", "name": "Coggs Web Craft and Responsive Templates", "note": "Coggs Web Craft landing page plus nine responsive template variants.", "url": "demos/webd300-ui-design/index.html"}, {"code": "WEBD121", "course": "WEBD121 — Web Development Fundamentals", "name": "Information Security Analyst", "note": "Three-page career site — the Associate's final web project.", "url": "demos/webd121-information-security/index.html"}, {"code": "WEBD121", "course": "WEBD121 — Web Development Fundamentals", "name": "Ye Music Notes", "note": "Five pages covering navigation, tables, forms, and multimedia.", "url": "demos/webd121-music-notes/index.html"}];
const COURSES = [{"code": "ENTD200", "title": "Fundamentals of Programming", "level": "as", "areas": ["programming"], "blurb": "Console applications with real problem domains: a car trip tracker, MPG calculators, and a payroll program with validated numeric input.", "tags": ["Python", "Functions", "Dictionaries", "Reports"], "writeups": {"slug": "fundamentals", "count": 2}}, {"code": "WEBD121", "title": "Web Development Fundamentals", "level": "as", "areas": ["web"], "blurb": "HTML and CSS from the ground up — navigation, tables, forms, multimedia, and a first pass at JavaScript, ending in a three-page career site.", "tags": ["HTML", "CSS", "Forms", "Multimedia"], "demo": "demos/webd121-information-security/index.html"}, {"code": "ITCC121", "title": "Introduction to Computer Science", "level": "as", "areas": ["systems"], "blurb": "Computing foundations: a software evaluation paper, a step-by-step PC setup guide, a database presentation, and SDLC waterfall work.", "tags": ["Hardware", "SDLC", "Databases"]}, {"code": "ITCC231", "title": "Introduction to Information Technology Writing", "level": "as", "areas": ["professional"], "blurb": "Technical writing in APA form — outline, rough draft, midterm project, and a final paper, with weekly discussion work.", "tags": ["APA", "Technical Writing", "Research"]}, {"code": "ITCC298", "title": "Computer Technology Intermediate Capstone", "level": "as", "areas": ["systems"], "blurb": "Associate's capstone: hardware requirements, a user manual, a presentation, a costing spreadsheet, and a final report.", "tags": ["Requirements", "Documentation", "Capstone"]}, {"code": "ITCC112", "title": "Advanced Productivity Applications", "level": "as", "areas": ["data", "professional"], "blurb": "Applied Excel — formatting, filtering, sorting, multi-sheet workbooks, freezing and views, page layout — with three graded workbook projects.", "tags": ["Excel", "Filtering", "Workbooks"]}, {"code": "ITMG221", "title": "IT Project Management", "level": "as", "areas": ["systems", "professional"], "blurb": "IT management through weekly case-study essays and structured review questions across eight weeks.", "tags": ["Case Studies", "IT Management"]}, {"code": "MGMT100", "title": "Human Relations", "level": "as", "areas": ["professional"], "blurb": "Interpersonal communication — a non-verbal communication essay, presentation preparation, and a final paper.", "tags": ["Communication", "Presentation"]}, {"code": "STEM185", "title": "The History and Context of STEM", "level": "as", "areas": ["professional"], "blurb": "Guided essay sequence with structured peer review, a timeline project, and a recorded video walkthrough.", "tags": ["Peer Review", "Essays"]}, {"code": "STEM270", "title": "Thinking and Acting Ethically", "level": "as", "areas": ["professional"], "blurb": "Applied ethics for technology: repeated case-study analyses and a code-of-ethics worksheet.", "tags": ["Ethics", "Case Analysis"]}, {"code": "ENTD220", "title": "Introduction to Python®", "level": "bs", "areas": ["programming"], "blurb": "The calculator rebuilt properly: dedicated functions, try/except handling, an imported Mylib module, a menu system, and finally classes with inheritance.", "tags": ["Python", "Modules", "OOP", "Exceptions"]}, {"code": "ENTD268", "title": "Information System Design", "level": "bs", "areas": ["systems"], "blurb": "Full analysis-and-design document set for one system — SRS with use cases, context and level-0 DFDs, UML, ERD, architecture, structure chart, and an SDD with test cases.", "tags": ["SRS", "SDD", "DFD", "UML", "ERD"]}, {"code": "ENTD120", "title": "User Experience I", "level": "bs", "areas": ["web", "systems"], "blurb": "UX research and design: an annotated bibliography, cognitive-mapping work, wireframes, and a final project paper.", "tags": ["UX", "Wireframes", "Research"]}, {"code": "WEBD221", "title": "Intermediate Web Development", "level": "bs", "areas": ["web"], "blurb": "A multi-page site grown a week at a time — semantic markup, stylesheets, imagery, JavaScript behaviour, and a validated form. The final site demonstrates the accumulated techniques.", "tags": ["HTML5", "CSS", "JavaScript", "Forms"], "demo": "demos/webd221-evolution-of-video-games/index.html"}, {"code": "ISSC297", "title": "Securing Applications", "level": "bs", "areas": ["security"], "blurb": "Ten hands-on application-security labs plus four case studies, worked against the OWASP testing guide and the CWE/SANS Top 25.", "tags": ["OWASP", "AppSec", "Labs"]}, {"code": "STEM470", "title": "Cybersecurity, Surveillance, Privacy and Ethics", "level": "bs", "areas": ["security", "professional"], "blurb": "Eight weeks on surveillance and privacy — facial recognition, predictive analytics, digital authoritarianism — ending in a case-study profile.", "tags": ["Privacy", "Surveillance", "Ethics"]}, {"code": "HRMT101", "title": "Human Relations Communication", "level": "bs", "areas": ["professional"], "blurb": "Communication styles, change management, and global virtual teams, closing with a presentation.", "tags": ["Communication", "Teams"], "writeups": {"slug": "hrmt101", "count": 3}}, {"code": "WEBD122", "title": "Introduction to Web Analytics", "level": "bs", "areas": ["data", "web"], "blurb": "Web data analysis — metrics selection, competitive intelligence, site critique methodology — delivered as weekly reports and two presentations.", "tags": ["Analytics", "Metrics", "Reporting"]}, {"code": "ISSC290", "title": "Securing Databases", "level": "bs", "areas": ["security", "databases"], "blurb": "Eight assignments on database hardening and access control, plus a researched paper taken from outline through draft to final.", "tags": ["Database Security", "Access Control"]}, {"code": "ENTD320", "title": "Intermediate Python® Programming", "level": "bs", "areas": ["programming", "web", "databases"], "blurb": "Flask from a hello-world route to two cooperating microservices over a shared SQLite database — with Jinja2 templates, a history page, and a unittest suite.", "tags": ["Flask", "Jinja2", "REST", "SQLite", "unittest"], "writeups": {"slug": "entd320", "count": 1}}, {"code": "INFO400", "title": "MongoDB® and Python®", "level": "bs", "areas": ["data", "databases"], "blurb": "The widest course in the degree: pandas and NumPy, REST and MongoDB, Cartopy mapping, Shapely geospatial dispatch, Apriori association rules, and scikit-learn — then a housing-price regression final.", "tags": ["pandas", "MongoDB", "scikit-learn", "Apriori", "Geospatial"], "writeups": {"slug": "info400", "count": 8}}, {"code": "INFO222", "title": "Database Concepts", "level": "bs", "areas": ["databases"], "blurb": "Relational fundamentals worked in SQLite against a medical-records schema, with seven assignments and a walkthrough of the build.", "tags": ["SQL", "SQLite", "Schema Design"]}, {"code": "ISSC221", "title": "Intermediate Computer Systems", "level": "bs", "areas": ["systems"], "blurb": "Twelve chapter write-ups on computer systems and architecture, consolidated into a final project.", "tags": ["Systems", "Architecture"]}, {"code": "INFO331", "title": "Management Information Systems", "level": "bs", "areas": ["systems", "professional"], "blurb": "Information systems in a business context, delivered as two recorded presentations with supporting written analysis.", "tags": ["MIS", "Presentations"]}, {"code": "STEM380", "title": "Coevolution of Society, Culture, and Technology", "level": "bs", "areas": ["professional"], "blurb": "Two researched papers and a final essay on how technology and society shape one another.", "tags": ["Research", "Technology & Society"], "writeups": {"slug": "stem380", "count": 5}}, {"code": "WEBD300", "title": "User Interface Design", "level": "bs", "areas": ["web"], "blurb": "A template family — default, blog, and portfolio — delivered three times over with dedicated desktop, tablet, and mobile stylesheets.", "tags": ["UI Design", "Responsive", "Templates"], "demo": "demos/webd300-ui-design/index.html"}, {"code": "WEBD241", "title": "Web Development Using JavaScript®", "level": "bs", "areas": ["web", "programming"], "blurb": "Seven JavaScript assignments — arrays and sorting, image galleries, form validation — collected behind a jQuery menu in the final project.", "tags": ["JavaScript", "DOM", "Validation", "jQuery"], "demo": "demos/webd241-javascript-final/FinalProject.html"}, {"code": "WEBD343", "title": "jQuery", "level": "bs", "areas": ["web"], "blurb": "Four runnable jQuery builds ending in a reusable accordion plugin — selectors and events, an accordion, an image slider, then the plugin rewrite.", "tags": ["jQuery", "Plugins", "Animation"], "demo": "demos/webd343-jquery/index.html"}, {"code": "INFO498", "title": "Information Technology: Capstone", "level": "bs", "areas": ["systems"], "blurb": "A point-of-sale system specified end to end — network topology, screen layout, project schedule, and a costed build.", "tags": ["Capstone", "Network Design", "Planning", "Costing"]}];
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



const el = (tag, cls, text) => {
    const node = document.createElement(tag);
    if (cls) node.className = cls;
    if (text !== undefined) node.textContent = text;
    return node;
};





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



function courseCard(course) {
    const card = el("article", "course" + (course.demo ? " has-demo" : ""));
    card.dataset.areas = course.areas.join(" ") + (course.demo ? " demo" : "");

    const top = el("div", "course-top");
    const lvl = el("span", "lvl " + course.level, course.level === "bs" ? "B.S." : "A.S.");
    top.appendChild(lvl);

    if (course.code) top.appendChild(el("span", "code", course.code));
    card.appendChild(top);

    card.appendChild(el("h3", null, course.title));
    card.appendChild(el("p", null, course.blurb));

    const tags = el("ul", "tags");
    course.tags.forEach((t) => tags.appendChild(el("li", null, t)));
    card.appendChild(tags);

    const actions = el("div", "actions");
    if (["INFO400", "ENTD320", "WEBD221", "WEBD241", "WEBD343", "WEBD300", "ENTD268", "INFO498"].includes(course.code)) { const detail = el("a", "link-btn", "Project Details"); detail.href = "coursework.html#project-" + course.code.toLowerCase(); actions.appendChild(detail); }
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

    const search = document.querySelector('#course-search');
    let active = 'all';
    const apply = (id) => {
        active = id;
        const words = (search?.value || '').toLowerCase().trim().split(/\s+/).filter(Boolean);
        let shown = 0;
        cards.forEach((card, index) => {
            const haystack = JSON.stringify(COURSES[index]).toLowerCase();
            const match = (id === "all" || card.dataset.areas.split(" ").includes(id)) && words.every(word => haystack.includes(word));
            card.hidden = !match;
            if (match) shown += 1;
        });
        if (count) {
            count.textContent =
                shown === COURSES.length
                    ? `${COURSES.length} courses · 2 degrees`
                    : `${shown} of ${COURSES.length} courses`;
        }
        const empty = document.querySelector('[data-empty]');
        if (empty) empty.hidden = shown !== 0;
    };
    search?.addEventListener('input', () => apply(active));

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





function wireTheme() {
    const root = document.documentElement;
    const toggle = document.querySelector("[data-theme-toggle]");

    let stored = null;
    try {
        stored = localStorage.getItem("portfolio-theme");
    } catch (e) {

    }
    if (stored === "light" || stored === "dark") root.dataset.theme = stored;

    if (!toggle) return;
    toggle.addEventListener("click", () => {

        const next = (root.dataset.theme || "light") === "light" ? "dark" : "light";
        root.dataset.theme = next;
        try {
            localStorage.setItem("portfolio-theme", next);
        } catch (e) {

        }
    });
}



renderDemos();
renderCourses();

wireTheme();


const menu = document.querySelector('.menu-toggle');
const nav = document.querySelector('#primary-nav');
if (menu && nav) {
    menu.hidden = false;
    document.documentElement.classList.add('has-menu');
    const closeMenu = () => { menu.setAttribute('aria-expanded', 'false'); nav.classList.remove('is-open'); };
    menu.addEventListener('click', () => {
        const open = menu.getAttribute('aria-expanded') !== 'true';
        menu.setAttribute('aria-expanded', String(open)); nav.classList.toggle('is-open', open);
    });
    nav.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
    document.addEventListener('keydown', event => { if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') { closeMenu(); menu.focus(); } });
    matchMedia('(min-width: 901px)').addEventListener('change', closeMenu);
}
document.querySelectorAll('[data-stat]').forEach(node => {
    const values = {courses: COURSES.length, demos: DEMOS.length, projects: PROJECTS.length};
    if (node.dataset.stat in values) node.textContent = values[node.dataset.stat];
});
try {
    const target = document.getElementById(decodeURIComponent(location.hash.slice(1)));
    if (target) target.scrollIntoView();
} catch { /* An invalid URL fragment must not interrupt page interactions. */ }
