from flask import Flask
app = Flask(_name_)
@app.route("/") # Route is a function which do route a user
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Nitish Kumar - Portfolio</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">

<style>
:root{
    --bg:#05070c;
    --panel:#0c1322;
    --glass:rgba(255,255,255,0.12);
    --primary:#4facfe;
    --secondary:#00f2fe;
    --accent:#ff4ecd;
    --text:#eaf0ff;
    --muted:#9aa4c7;
}

/* ================= RESET ================= */
*{
    box-sizing:border-box;
    scroll-behavior:smooth;
}

body{
    margin:0;
    font-family:"Poppins",sans-serif;
    min-height:100vh;
    color:var(--text);

    background:
      radial-gradient(circle at 20% 10%, #11234a, transparent 40%),
      radial-gradient(circle at 80% 20%, #2d0b45, transparent 45%),
      radial-gradient(circle at 50% 80%, #061a2f, transparent 55%),
      linear-gradient(180deg,#020409,#040818);

    display:flex;
    overflow-x:hidden;
}

/* ================= SIDEBAR ================= */
.sidebar{
    width:230px;
    background:linear-gradient(180deg,#070b18,#090f24);
    padding:40px 25px;
    height:100vh;
    position:fixed;
    box-shadow:10px 0 60px rgba(0,0,0,0.85);
    z-index:10;
}

.sidebar img{
    width:120px;
    height:120px;
    border-radius:50%;
    display:block;
    margin:auto;
    margin-bottom:20px;

    border:3px solid transparent;
    background:
      linear-gradient(#000,#000) padding-box,
      linear-gradient(135deg,var(--primary),var(--accent)) border-box;

    box-shadow:0 0 40px rgba(79,172,254,0.6);
}

.sidebar h2{
    text-align:center;
    font-weight:600;
    letter-spacing:0.5px;
}

.sidebar a{
    display:block;
    padding:14px;
    margin:10px 0;
    text-decoration:none;
    color:var(--text);
    border-radius:14px;
    text-align:center;
    font-weight:500;
    transition:0.35s;
}

.sidebar a:hover{
    background:linear-gradient(
        135deg,
        rgba(79,172,254,0.25),
        rgba(255,78,205,0.25)
    );
    box-shadow:0 0 20px rgba(79,172,254,0.35);
    transform:translateX(8px);
}

/* ================= CONTENT ================= */
.content{
    flex:1;
    margin-left:230px;
    padding:50px;
}

section{margin-bottom:110px;}
h1{
    color:var(--primary);
    font-weight:700;
    letter-spacing:1px;
}

/* ================= HERO ================= */
.hero{
    position:relative;
    padding:120px 50px;
    border-radius:35px;
    text-align:center;

    background:
      linear-gradient(120deg,
        rgba(79,172,254,0.35),
        rgba(255,78,205,0.35),
        rgba(0,242,254,0.35)
      ),
      radial-gradient(circle at top,#0d2345,#050816);

    background-size:400% 400%;
    animation:aurora 14s ease infinite;

    box-shadow:
      0 50px 120px rgba(0,0,0,0.9),
      inset 0 0 60px rgba(255,255,255,0.08);

    opacity:0;
    transform:translateY(40px) scale(1.05);
}

/* hero wipe */
.hero::before{
    content:"";
    position:absolute;
    inset:-50%;
    background:linear-gradient(
        45deg,
        transparent 40%,
        rgba(255,255,255,0.25) 50%,
        transparent 60%
    );
    transform:translateX(-120%);
}

/* text start */
.hero h1,
.hero p{
    opacity:0;
    transform:translateY(30px);
    filter:blur(6px);
}

.hero.active{
    opacity:1;
    transform:translateY(0) scale(1);
    transition:1.3s cubic-bezier(.19,1,.22,1);
}

.hero.active::before{
    animation:wipe 1.5s ease forwards;
}

.hero.active h1{
    animation:textIn 1s ease forwards;
    animation-delay:0.4s;
}

.hero.active p{
    animation:textIn 1s ease forwards;
    animation-delay:0.7s;
    color:var(--muted);
    font-size:1.1rem;
}

/* ================= GLASS ================= */
.glass{
    background:
      linear-gradient(
        135deg,
        rgba(255,255,255,0.22),
        rgba(255,255,255,0.06)
      );

    backdrop-filter:blur(18px);
    border-radius:24px;
    padding:28px;

    border:1px solid rgba(255,255,255,0.25);

    box-shadow:
      0 25px 80px rgba(0,0,0,0.75),
      inset 0 0 30px rgba(255,255,255,0.08);

    transition:0.45s;
}

.glass:hover{
    transform:translateY(-14px) scale(1.02);
    box-shadow:
      0 35px 120px rgba(79,172,254,0.45),
      inset 0 0 40px rgba(255,255,255,0.1);
}

/* ================= LAYOUT ================= */
.flex{
    display:flex;
    flex-wrap:wrap;
    gap:30px;
}

.card{
    width:320px;
}

.timeline{
    border-left:3px solid transparent;
    border-image:linear-gradient(var(--primary),var(--accent)) 1;
    padding-left:32px;
}

.tl-item{margin-bottom:35px;}

/* ================= FORM ================= */
form input,
form textarea{
    width:100%;
    padding:14px;
    margin:12px 0;
    border-radius:16px;
    border:1px solid rgba(255,255,255,0.2);
    background:#0a1224;
    color:white;
    font-size:0.95rem;
}

form input:focus,
form textarea:focus{
    outline:none;
    border-color:var(--primary);
    box-shadow:0 0 15px rgba(79,172,254,0.5);
}

form button{
    padding:14px 30px;
    border:none;
    border-radius:26px;
    background:linear-gradient(135deg,var(--primary),var(--accent));
    color:white;
    font-weight:600;
    letter-spacing:0.5px;
    cursor:pointer;
    box-shadow:0 10px 30px rgba(79,172,254,0.5);
}

/* ================= ANIMATIONS ================= */
@keyframes wipe{
    to{transform:translateX(120%);}
}

@keyframes textIn{
    to{
        opacity:1;
        transform:none;
        filter:none;
    }
}

@keyframes aurora{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

/* ================= MOBILE ================= */
@media(max-width:900px){
    .sidebar{
        position:relative;
        width:100%;
        height:auto;
    }
    .content{
        margin-left:0;
        padding:30px;
    }
}
</style>

</head>
<body>

<!-- SIDEBAR -->
<div class="sidebar">
    <img src="https://via.placeholder.com/150">
    <h2>Nitish Kumar Gupta</h2>

    <a href="#hero">Home</a>
    <a href="#about">About</a>
    <a href="#services">Services</a>
    <a href="#projects">Projects</a>
    <a href="#experience">Experience</a>
    <a href="#education">Education</a>
    <a href="#testimonials">Testimonials</a>
    <a href="#skills">Skills</a>
    <a href="#contact">Contact</a>

    <div class="toggle-btn" onclick="toggleDark()">🌙 Dark Mode</div>
</div>

<!-- CONTENT -->
<div class="content">

    <!-- HERO -->
    <section id="hero" class="hero">
        <div class="particle" style="left:10%; animation-duration: 8s;"></div>
        <div class="particle" style="left:50%; animation-duration: 12s;"></div>
        <div class="particle" style="left:80%; animation-duration: 9s;"></div>

        <h1>Hi, I'm <span style="color: var(--accent);">Nitish Kumar Gupta</span></h1>
        <div class="typing">Cyber securtiy student</div>
    </section>

    <!-- ABOUT -->
    <section id="about">
        <h1>About Me</h1>
        <p>
            I am a passionate software developer with experience in frontend development, design,
            UI/UX, animations, and building high-quality digital experiences with a focus on
            creativity, performance, and modern aesthetics.
        </p>
    </section>

    <!-- SERVICES -->
    <section id="services">
        <h1>Services</h1>
        <div class="flex">
            <div class="glass card"><h2>Frontend Development</h2><p>Responsive, modern websites built professionally.</p></div>
            <div class="glass card"><h2>UI/UX Design</h2><p>Clean interfaces with smooth interactions.</p></div>
            <div class="glass card"><h2>Branding</h2><p>Logos, visual identity, and brand design.</p></div>
        </div>
    </section>

    <!-- PROJECTS -->
    <section id="projects">
        <h1>Projects</h1>
        <div class="flex">
            <div class="glass card"><h2>Nayasa - Circular Economic Marketplace</h2><p>Interactive UI with animations.</p>
            <a href="https://lilsh4050.github.io/NayaSa-Circular-Economic-Marketplace/">Visit Project </a></div>
        </div>
    </section>

    <!-- EXPERIENCE -->
    <section id="experience">
        <h1>Experience</h1>
        <div class="timeline">
            <div class="tl-item">
                <h3>Graphic Designer - Skillcraft Technology </h3>
                <p>June–August, 2025</p>
            </div>
        </div>
    </section>

    <!-- EDUCATION -->
    <section id="education">
        <h1>Education</h1>
        <div class="timeline">
            <div class="tl-item">
                <h3>BTech-Computer Science</h3>
                <p>2024–2028</p>
            </div>
        </div>
    </section>

    <!-- SKILLS -->
    <section id="skills">
        <h1>Skills</h1>
        <div class="flex">
            <div class="glass card">HTML</div>
            <div class="glass card">CSS</div>
            <div class="glass card">Canva</div>
            <div class="glass card">Photoshop</div>
            <div class="glass card">Python</div>
            <div class="glass card">Adobe</div>
            <div class="glass card">UI/UX</div>
        </div>
    </section>

    <!-- CONTACT -->
    <section id="contact">
        <h1>Contact</h1>
        <form>
            <input type="text" placeholder="Your Name">
            <input type="email" placeholder="Enter Email">
            <textarea rows="6" placeholder="Your Message"></textarea>
            <button>Send Message</button>
        </form>
    </section>

</div>

<script>
function toggleDark() {
    document.body.classList.toggle("dark");
}
</script>

</body>
</html>
"""
@app.route("/about")
def abouta():
    return """
    <h1>jhurgiwrubhviurgwr</h1>
    """

if _name=='main_':
    app.run(debug = True)