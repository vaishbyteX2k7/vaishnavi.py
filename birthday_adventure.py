"""
Happy Birthday Website — "Adventure Awaits" Edition
-----------------------------------------------------
A cute, adventure-themed birthday site built with Flask.
Follow a little dotted trail across a map, unlock playful
badges at each stop, flip through a photo gallery, open a
sealed letter, blow out candles, and open the treasure chest
for a confetti burst + birthday wish.

Folder structure required:
    birthday_adventure.py
    static/
        images/
            photo1.jpg
            photo2.jpg
            photo3.jpg
            photo4.jpg

Setup:
    pip install flask --break-system-packages
    python birthday_adventure.py

Then open http://127.0.0.1:5000
"""

from flask import Flask, render_template_string, url_for

app = Flask(__name__)

# ---- Personalize here ----
NAME = "Friend"
AGE_LABEL = "Level 24"          # e.g. "Level 24", or leave as "" to hide
FINAL_WISH = "Shine just like this Diamond."

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Happy Birthday, {{ name }}! 🎈</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@500;700;800&family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  :root{
    --cream:#FBF3E2;
    --parchment:#F3E3C3;
    --teal:#2A9D8F;
    --teal-dark:#1F7A6E;
    --coral:#FF6F59;
    --mustard:#F4A261;
    --navy:#274156;
    --line:#C9A66B;
  }
  *{box-sizing:border-box; margin:0; padding:0;}
  html{scroll-behavior:smooth;}
  body{
    background:var(--cream);
    color:var(--navy);
    font-family:'Nunito', sans-serif;
    overflow-x:hidden;
    position:relative;
  }
  h1,h2,h3{ font-family:'Baloo 2', sans-serif; }

  /* faint map texture */
  body::before{
    content:"";
    position:fixed; inset:0; z-index:0;
    background-image:
      radial-gradient(var(--line) 1px, transparent 1px);
    background-size:26px 26px;
    opacity:0.12;
    pointer-events:none;
  }
  section, header, footer{ position:relative; z-index:1; }

  /* ---------- Hero ---------- */
  header{
    min-height:100vh;
    display:flex; flex-direction:column; align-items:center; justify-content:center;
    text-align:center; padding:40px 20px;
  }
  .badge{
    font-family:'Baloo 2', sans-serif;
    font-size:0.85rem; font-weight:700;
    background:var(--coral); color:white;
    padding:6px 18px; border-radius:999px;
    margin-bottom:26px; letter-spacing:0.02em;
    box-shadow:0 4px 0 rgba(0,0,0,0.08);
  }
  h1{
    font-size:clamp(2.6rem, 8vw, 5rem);
    font-weight:800; color:var(--teal-dark);
    line-height:1.05;
    text-shadow:3px 3px 0 var(--mustard);
  }
  header p.sub{
    margin-top:22px; max-width:480px;
    font-size:1.1rem; font-weight:600; color:var(--navy);
    opacity:0.85;
  }

  /* hot air balloon (also poppable) */
  .balloon{
    position:absolute; font-size:3.2rem;
    animation:drift 9s ease-in-out infinite;
    filter:drop-shadow(2px 4px 3px rgba(0,0,0,0.15));
    cursor:pointer;
    transition:transform 0.15s ease, opacity 0.25s ease;
  }
  .balloon.b1{ top:10%; left:8%; animation-delay:0s; }
  .balloon.b2{ top:18%; right:10%; animation-delay:1.5s; font-size:2.4rem; }
  .balloon.b3{ top:6%; left:48%; animation-delay:3s; font-size:2rem; }
  @keyframes drift{
    0%,100%{ transform:translateY(0) rotate(-3deg); }
    50%{ transform:translateY(-22px) rotate(3deg); }
  }
  .balloon.popped{
    animation:none;
    transform:scale(1.5);
    opacity:0;
  }
  .balloon-hint{
    margin-top:10px; font-size:0.7rem; font-weight:700;
    letter-spacing:0.05em; color:var(--teal-dark); opacity:0.5;
  }

  /* ---------- Birthday cake + candles ---------- */
  .cake-section{
    max-width:640px; margin:0 auto; padding:20px 24px 100px;
    text-align:center;
  }
  .cake-section h2{
    color:var(--teal-dark); font-size:clamp(1.8rem,4vw,2.4rem); margin-bottom:10px;
  }
  .cake-section > p{ font-weight:600; opacity:0.75; margin-bottom:50px; }
  .candles{
    display:flex; justify-content:center; gap:22px; margin-bottom:0;
  }
  .candle{
    position:relative; width:16px; height:64px; cursor:pointer;
    background:linear-gradient(180deg, #ffffff, var(--parchment));
    border-radius:5px; border:2px solid var(--line);
  }
  .candle::before{
    content:""; position:absolute; top:-8px; left:50%; transform:translateX(-50%);
    width:2px; height:8px; background:#3b3225;
  }
  .flame{
    position:absolute; top:-28px; left:50%; transform:translateX(-50%);
    width:14px; height:22px;
    background:radial-gradient(circle at 50% 70%, #fff6d5 0%, var(--mustard) 35%, var(--coral) 70%, transparent 75%);
    border-radius:50% 50% 50% 50% / 60% 60% 40% 40%;
    animation:flicker 1.5s ease-in-out infinite;
    transition:opacity 0.3s ease, transform 0.3s ease;
    filter:drop-shadow(0 0 8px rgba(244,162,97,0.7));
  }
  @keyframes flicker{
    0%,100%{ transform:translateX(-50%) scale(1) rotate(-2deg); }
    50%{ transform:translateX(-50%) scale(1.08,0.94) rotate(2deg); }
  }
  .candle.blown .flame{
    opacity:0; transform:translateX(-50%) translateY(-10px) scale(0.4);
  }
  .candle .smoke{
    position:absolute; top:-32px; left:50%; transform:translateX(-50%);
    width:3px; height:16px; background:rgba(120,120,120,0.35);
    border-radius:4px; opacity:0;
  }
  .candle.blown .smoke{ animation:rise 1.4s ease-out forwards; }
  @keyframes rise{
    0%{ opacity:0.6; transform:translate(-50%,0) scaleY(1); }
    100%{ opacity:0; transform:translate(-50%,-26px) scaleY(2); }
  }
  .cake-base{
    width:220px; height:56px; margin:0 auto;
    background:linear-gradient(180deg, var(--coral), #E85A45);
    border-radius:14px 14px 30px 30px;
    box-shadow:0 4px 0 rgba(0,0,0,0.08);
  }
  .cake-hint{
    margin-top:22px; font-size:0.8rem; font-weight:700;
    letter-spacing:0.05em; color:var(--navy); opacity:0.55;
  }
  .cake-wish{
    margin-top:16px; font-family:'Baloo 2', sans-serif; font-weight:700;
    font-size:1.25rem; color:var(--teal-dark);
    opacity:0; transform:translateY(8px);
    transition:opacity 0.6s ease, transform 0.6s ease;
  }
  .cake-section.all-blown .cake-wish{ opacity:1; transform:translateY(0); }

  /* ---------- Panda couple ---------- */
  .pandas{
    max-width:640px; margin:0 auto; padding:20px 24px 110px;
    text-align:center;
  }
  .pandas h2{
    color:var(--teal-dark); font-size:clamp(1.8rem,4vw,2.4rem); margin-bottom:10px;
  }
  .pandas > p{ font-weight:600; opacity:0.75; margin-bottom:50px; }
  .panda-pair{
    display:flex; align-items:center; justify-content:center; gap:26px;
  }
  .panda-heart{ font-size:1.8rem; animation:pulse 1.6s ease-in-out infinite; }
  @keyframes pulse{ 0%,100%{transform:scale(1);} 50%{transform:scale(1.2);} }
  .panda{ position:relative; width:120px; height:120px; }
  .panda .ear{
    position:absolute; width:34px; height:34px; background:var(--navy);
    border-radius:50%; top:-6px;
  }
  .panda .ear.left{ left:-4px; }
  .panda .ear.right{ right:-4px; }
  .panda .face{
    position:absolute; inset:8px; background:var(--cream);
    border:3px solid var(--navy); border-radius:50%;
  }
  .panda .patch{
    position:absolute; width:30px; height:38px; background:var(--navy);
    border-radius:50%; top:34px;
  }
  .panda .patch.left{ left:8px; transform:rotate(-8deg); }
  .panda .patch.right{ right:8px; transform:rotate(8deg); }
  .panda .eye{
    position:absolute; width:8px; height:8px; background:var(--cream);
    border-radius:50%; top:48px;
  }
  .panda .eye.left{ left:20px; }
  .panda .eye.right{ right:20px; }
  .panda .nose{
    position:absolute; width:10px; height:8px; background:var(--navy);
    border-radius:50%; top:60px; left:50%; transform:translateX(-50%);
  }
  .panda.right .ear, .panda.right .patch{ background:#3a2f1f; }
  .panda-caption{
    margin-top:22px; font-family:'Baloo 2', sans-serif; font-weight:700;
    font-size:1.1rem; color:var(--navy); opacity:0.85;
  }

  /* ---------- Photo gallery ---------- */
  .gallery{
    max-width:720px; margin:0 auto; padding:20px 24px 110px;
    text-align:center;
  }
  .gallery h2{
    color:var(--teal-dark); font-size:clamp(1.8rem,4vw,2.4rem); margin-bottom:10px;
  }
  .gallery > p{ font-weight:600; opacity:0.75; margin-bottom:44px; }
  .gallery-grid{
    display:grid; grid-template-columns:repeat(2, 1fr); gap:22px;
  }
  .photo-card{
    position:relative; aspect-ratio:3/4; cursor:pointer;
    perspective:1000px;
  }
  .photo-card-inner{
    position:relative; width:100%; height:100%;
    transition:transform 0.6s cubic-bezier(.2,.8,.2,1);
    transform-style:preserve-3d;
    border-radius:16px;
    box-shadow:0 4px 0 var(--parchment);
  }
  .photo-card.flipped .photo-card-inner{ transform:rotateY(180deg); }
  .photo-face{
    position:absolute; inset:0;
    -webkit-backface-visibility:hidden; backface-visibility:hidden;
    border-radius:16px; overflow:hidden;
    border:3px solid white;
  }
  .photo-face img{ width:100%; height:100%; object-fit:cover; display:block; }
  .photo-face.back{
    transform:rotateY(180deg);
    background:var(--teal);
    display:flex; align-items:center; justify-content:center;
    padding:16px; text-align:center;
  }
  .photo-face.back p{
    font-family:'Baloo 2', sans-serif; font-weight:700;
    color:white; font-size:0.95rem; line-height:1.4;
  }
  .gallery-hint{
    margin-top:26px; font-size:0.8rem; font-weight:700;
    letter-spacing:0.05em; color:var(--navy); opacity:0.55;
  }

  /* ---------- Birthday letter ---------- */
  .letter-section{
    max-width:600px; margin:0 auto; padding:20px 24px 130px;
    text-align:center;
  }
  .letter-section h2{
    color:var(--teal-dark); font-size:clamp(1.8rem,4vw,2.4rem); margin-bottom:10px;
  }
  .letter-section > p.lead{ font-weight:600; opacity:0.75; margin-bottom:44px; }
  .envelope{
    position:relative; width:220px; height:150px; margin:0 auto;
    cursor:pointer;
  }
  .envelope-body{
    position:absolute; inset:0;
    background:var(--teal); border-radius:8px;
    box-shadow:0 4px 0 var(--teal-dark);
  }
  .envelope-flap{
    position:absolute; top:0; left:0; width:0; height:0;
    border-left:110px solid transparent;
    border-right:110px solid transparent;
    border-top:75px solid var(--teal-dark);
    transform-origin:top;
    transition:transform 0.5s ease;
    z-index:2;
  }
  .envelope.open .envelope-flap{ transform:rotateX(180deg); }
  .envelope-heart{
    position:absolute; top:56%; left:50%; transform:translate(-50%,-50%);
    font-size:1.6rem; z-index:1;
  }
  .letter-hint{
    margin-top:20px; font-size:0.8rem; font-weight:700;
    letter-spacing:0.05em; color:var(--navy); opacity:0.55;
  }
  .letter-paper{
    max-width:480px; margin:34px auto 0;
    background:white; border-radius:6px;
    border:2px solid var(--parchment);
    box-shadow:0 4px 0 var(--parchment);
    padding:34px 30px;
    text-align:left;
    font-family:'Baloo 2', sans-serif;
    color:var(--navy);
    opacity:0; transform:translateY(14px) scale(0.98);
    max-height:0; overflow:hidden;
    transition:opacity 0.6s ease, transform 0.6s ease;
  }
  .letter-section.open .letter-paper{
    opacity:1; transform:translateY(0) scale(1);
    max-height:600px; margin-top:34px; padding:34px 30px;
  }
  .letter-paper .salutation{ font-size:1.15rem; font-weight:700; margin-bottom:16px; }
  .letter-paper p{ font-size:1rem; line-height:1.7; font-weight:400; margin-bottom:14px; }
  .letter-paper .signoff{ margin-top:10px; font-weight:700; }
    margin-top:56px; font-weight:700; font-size:0.85rem;
    color:var(--teal-dark); opacity:0.7;
    display:flex; flex-direction:column; align-items:center; gap:6px;
  }
  .cue .arrow{ animation:bounce 1.6s ease-in-out infinite; }
  @keyframes bounce{ 0%,100%{transform:translateY(0);} 50%{transform:translateY(8px);} }

  /* ---------- Trail ---------- */
  .trail{
    max-width:720px; margin:0 auto; padding:100px 24px 60px;
  }
  .trail h2{
    text-align:center; color:var(--teal-dark);
    font-size:clamp(1.8rem,4vw,2.4rem); margin-bottom:16px;
  }
  .trail > p{
    text-align:center; font-weight:600; opacity:0.75; margin-bottom:60px;
  }
  .stops{ position:relative; padding-left:38px; }
  .stops::before{
    content:"";
    position:absolute; left:9px; top:6px; bottom:6px; width:3px;
    background-repeat:repeat-y;
    background-image:linear-gradient(var(--line) 60%, transparent 40%);
    background-size:3px 14px;
  }
  .stop{
    position:relative; margin-bottom:34px; cursor:pointer;
  }
  .stop::before{
    content:"";
    position:absolute; left:-38px; top:4px;
    width:20px; height:20px; border-radius:50%;
    background:var(--mustard); border:3px solid var(--cream);
    box-shadow:0 0 0 2px var(--line);
    transition:background 0.3s ease, transform 0.3s ease;
  }
  .stop.open::before{ background:var(--teal); transform:scale(1.15); }
  .stop-card{
    background:white; border:2px solid var(--parchment);
    border-radius:16px; padding:18px 22px;
    box-shadow:0 3px 0 var(--parchment);
    transition:transform 0.25s ease;
  }
  .stop-card:hover{ transform:translateX(4px); }
  .stop-card h3{
    color:var(--navy); font-size:1.15rem; display:flex; align-items:center; gap:10px;
  }
  .stop-card .icon{ font-size:1.3rem; }
  .stop-card p{
    margin-top:8px; font-size:0.95rem; font-weight:600; color:var(--navy);
    opacity:0; max-height:0; overflow:hidden;
    transition:opacity 0.35s ease, max-height 0.35s ease, margin-top 0.35s ease;
  }
  .stop.open .stop-card p{ opacity:0.85; max-height:100px; margin-top:8px; }

  /* ---------- Treasure ---------- */
  .treasure{
    text-align:center; padding:40px 24px 130px;
  }
  .treasure p.lead{ font-weight:700; opacity:0.8; margin-bottom:26px; }
  .chest{
    font-size:5.5rem; cursor:pointer; display:inline-block;
    transition:transform 0.25s ease;
    filter:drop-shadow(3px 5px 3px rgba(0,0,0,0.15));
  }
  .chest:hover{ transform:scale(1.06) rotate(-2deg); }
  .chest.opened{ transform:scale(1.1); }
  .wish-reveal{
    margin-top:30px; max-width:480px; margin-left:auto; margin-right:auto;
    font-family:'Baloo 2', sans-serif; font-weight:700;
    font-size:1.4rem; color:var(--teal-dark);
    opacity:0; transform:translateY(10px);
    transition:opacity 0.6s ease, transform 0.6s ease;
  }
  .treasure.opened .wish-reveal{ opacity:1; transform:translateY(0); }
  .hint{
    margin-top:16px; font-size:0.8rem; font-weight:700;
    letter-spacing:0.05em; color:var(--navy); opacity:0.55;
  }

  .confetti-piece{
    position:fixed; top:50%; left:50%; width:9px; height:12px;
    z-index:5; pointer-events:none;
  }

  /* ---------- Balloon pop mini-game ---------- */
  .pop-section{
    max-width:680px; margin:0 auto; padding:20px 24px 110px;
    text-align:center;
  }
  .pop-section h2{
    color:var(--teal-dark); font-size:clamp(1.8rem,4vw,2.4rem); margin-bottom:10px;
  }
  .pop-section > p{ font-weight:600; opacity:0.75; margin-bottom:12px; }
  .pop-count{
    font-family:'Baloo 2', sans-serif; font-weight:700;
    color:var(--coral); font-size:1rem; margin-bottom:36px;
  }
  .pop-field{
    position:relative; display:flex; flex-wrap:wrap;
    justify-content:center; gap:26px 30px; min-height:170px;
  }
  .pop-balloon{
    font-size:3rem; cursor:pointer; user-select:none;
    animation:bob 3s ease-in-out infinite;
    transition:transform 0.15s ease, opacity 0.25s ease;
    filter:drop-shadow(2px 4px 3px rgba(0,0,0,0.15));
  }
  .pop-balloon:nth-child(2n){ animation-delay:0.4s; }
  .pop-balloon:nth-child(3n){ animation-delay:0.9s; }
  .pop-balloon:nth-child(4n){ animation-delay:1.3s; }
  @keyframes bob{
    0%,100%{ transform:translateY(0); }
    50%{ transform:translateY(-12px); }
  }
  .pop-balloon.popped{
    animation:none;
    transform:scale(1.6);
    opacity:0;
    pointer-events:none;
  }

  /* ---------- Hearts boom button ---------- */
  .hearts-section{
    max-width:480px; margin:0 auto; padding:0 24px 130px;
    text-align:center;
  }
  .hearts-section h2{
    color:var(--teal-dark); font-size:clamp(1.8rem,4vw,2.4rem); margin-bottom:10px;
  }
  .hearts-section > p{ font-weight:600; opacity:0.75; margin-bottom:40px; }
  .heart-button{
    font-size:4.2rem; cursor:pointer; display:inline-block;
    transition:transform 0.2s ease;
    filter:drop-shadow(2px 4px 3px rgba(0,0,0,0.15));
  }
  .heart-button:hover{ transform:scale(1.1); }
  .heart-button:active{ transform:scale(0.92); }
  .hearts-hint{
    margin-top:18px; font-size:0.8rem; font-weight:700;
    letter-spacing:0.05em; color:var(--navy); opacity:0.55;
  }
  .heart-piece{
    position:fixed; z-index:5; pointer-events:none;
    font-size:1.4rem;
  }

  footer{
    text-align:center; padding:40px 24px;
    font-weight:700; font-size:0.8rem; color:var(--navy); opacity:0.5;
  }

  @media (prefers-reduced-motion: reduce){
    *{ animation:none !important; transition:none !important; }
  }
</style>
</head>
<body>

<header>
  <span class="balloon b1" data-balloon>🎈</span>
  <span class="balloon b2" data-balloon>🎈</span>
  <span class="balloon b3" data-balloon>🎈</span>

  {% if age_label %}<div class="badge">{{ age_label }} Unlocked</div>{% endif %}
  <h1>Happy Birthday,<br>{{ name }}!</h1>
  <p class="sub">Grab your compass — there's a little adventure waiting before the cake.</p>
  <div class="balloon-hint">psst — the balloons are poppable</div>

  <div class="cue">
    <span>follow the trail</span>
    <span class="arrow">↓</span>
  </div>
</header>

<section class="trail">
  <h2>The Trail So Far</h2>
  <p>Tap each stop to open it</p>

  <div class="stops">
    <div class="stop">
      <div class="stop-card">
        <h3><span class="icon">🧭</span> Stop 1 — The Beginning</h3>
        <p>Every great story needs an unforgettable lead character. Lucky for this one, it's you.</p>
      </div>
    </div>
    <div class="stop">
      <div class="stop-card">
        <h3><span class="icon">⛰️</span> Stop 2 — The Climb</h3>
        <p>The tricky years, the plot twists, the "how did I even get through that" moments — all cleared.</p>
      </div>
    </div>
    <div class="stop">
      <div class="stop-card">
        <h3><span class="icon">🌊</span> Stop 3 — The Current Chapter</h3>
        <p>Right here, right now. Older, wiser, and somehow still up for anything.</p>
      </div>
    </div>
    <div class="stop">
      <div class="stop-card">
        <h3><span class="icon">🔥</span> Stop 4 — What's Next</h3>
        <p>A whole new year of chapters, still unwritten. That's the exciting part.</p>
      </div>
    </div>
  </div>
</section>

<section class="cake-section" id="cakeSection">
  <h2>Make a Wish</h2>
  <p>Blow out each candle, one by one</p>

  <div class="candles">
    <div class="candle" data-candle><div class="flame"></div><div class="smoke"></div></div>
    <div class="candle" data-candle><div class="flame"></div><div class="smoke"></div></div>
    <div class="candle" data-candle><div class="flame"></div><div class="smoke"></div></div>
    <div class="candle" data-candle><div class="flame"></div><div class="smoke"></div></div>
    <div class="candle" data-candle><div class="flame"></div><div class="smoke"></div></div>
  </div>
  <div class="cake-base"></div>
  <div class="cake-hint" id="cakeHint">tap each flame to blow it out</div>
  <div class="cake-wish">Wish made. The universe is now legally obligated to deliver.</div>
</section>

<section class="pandas">
  <h2>Your Adventure Buddies</h2>
  <p>Two pandas, one bamboo forest, zero notes</p>

  <div class="panda-pair">
    <div class="panda left">
      <div class="ear left"></div>
      <div class="ear right"></div>
      <div class="face">
        <div class="patch left"></div>
        <div class="patch right"></div>
        <div class="eye left"></div>
        <div class="eye right"></div>
        <div class="nose"></div>
      </div>
    </div>
    <span class="panda-heart">💕</span>
    <div class="panda right">
      <div class="ear left"></div>
      <div class="ear right"></div>
      <div class="face">
        <div class="patch left"></div>
        <div class="patch right"></div>
        <div class="eye left"></div>
        <div class="eye right"></div>
        <div class="nose"></div>
      </div>
    </div>
  </div>
  <div class="panda-caption">Inseparable, snack-motivated, and rooting for you today.</div>
</section>

<section class="gallery">
  <h2>Snapshots From the Road</h2>
  <p>Tap a photo to flip it over</p>

  <div class="gallery-grid">
    <div class="photo-card" data-flip>
      <div class="photo-card-inner">
        <div class="photo-face front"><img src="{{ photo1 }}" alt="Adventure photo 1"></div>
        <div class="photo-face back"><p>Breaking news: you're still the main character.</p></div>
      </div>
    </div>
    <div class="photo-card" data-flip>
      <div class="photo-card-inner">
        <div class="photo-face front"><img src="{{ photo2 }}" alt="Adventure photo 2"></div>
        <div class="photo-face back"><p>Dancing under the same moon, one more year in.</p></div>
      </div>
    </div>
    <div class="photo-card" data-flip>
      <div class="photo-card-inner">
        <div class="photo-face front"><img src="{{ photo3 }}" alt="Adventure photo 3"></div>
        <div class="photo-face back"><p>Always in your corner, chin resting on your shoulder.</p></div>
      </div>
    </div>
    <div class="photo-card" data-flip>
      <div class="photo-card-inner">
        <div class="photo-face front"><img src="{{ photo4 }}" alt="Adventure photo 4"></div>
        <div class="photo-face back"><p>Peace signs up — the whole world's still ahead of you.</p></div>
      </div>
    </div>
  </div>
  <div class="gallery-hint">tap each one, they all flip back too</div>
</section>

<section class="pop-section">
  <h2>Pop for Luck</h2>
  <p>Tap every balloon before they float off</p>
  <div class="pop-count" id="popCount">0 / 8 popped</div>

  <div class="pop-field" id="popField">
    <span class="pop-balloon" data-pop style="color:#FF6F59">🎈</span>
    <span class="pop-balloon" data-pop style="color:#2A9D8F">🎈</span>
    <span class="pop-balloon" data-pop style="color:#F4A261">🎈</span>
    <span class="pop-balloon" data-pop style="color:#274156">🎈</span>
    <span class="pop-balloon" data-pop style="color:#FF6F59">🎈</span>
    <span class="pop-balloon" data-pop style="color:#2A9D8F">🎈</span>
    <span class="pop-balloon" data-pop style="color:#F4A261">🎈</span>
    <span class="pop-balloon" data-pop style="color:#274156">🎈</span>
  </div>
</section>

<section class="hearts-section">
  <h2>Send Some Love</h2>
  <p>Tap the heart and let it rain</p>
  <div class="heart-button" id="heartButton">💗</div>
  <div class="hearts-hint">tap it as many times as you like</div>
</section>

<section class="letter-section" id="letterSection">
  <h2>One More Thing</h2>
  <p class="lead">A little letter, sealed just for today</p>

  <div class="envelope" id="envelope">
    <div class="envelope-body"></div>
    <div class="envelope-heart">💌</div>
    <div class="envelope-flap"></div>
  </div>
  <div class="letter-hint" id="letterHint">tap the envelope to open it</div>

  <div class="letter-paper">
    <div class="salutation">Dear {{ name }},</div>
    <p>Another year has quietly turned over, and somehow you've made every version of it look easy — even the parts that weren't.</p>
    <p>{{ final_wish }} May this year hand you more reasons to laugh too hard, wander too far, and stay up too late talking about nothing in particular.</p>
    <p>Whatever adventure finds you next, I hope I get a front-row seat to it.</p>
    <div class="signoff">Happy birthday. — With love</div>
  </div>
</section>

<section class="treasure" id="treasure">
  <p class="lead">You made it to the end of the trail.</p>
  <div class="chest" id="chest">🎁</div>
  <div class="hint" id="chestHint">tap to open</div>
  <div class="wish-reveal">{{ final_wish }}</div>
</section>

<footer>Made with adventure &amp; a little bit of glitter</footer>

<script>
  const CONFETTI_COLORS = ['#2A9D8F','#FF6F59','#F4A261','#274156','#F3E3C3'];

  // Reusable confetti burst from a given screen point
  function spawnConfetti(originX, originY, count = 50, spread = 260) {
    for (let i = 0; i < count; i++) {
      const p = document.createElement('div');
      p.className = 'confetti-piece';
      p.style.background = CONFETTI_COLORS[Math.floor(Math.random() * CONFETTI_COLORS.length)];
      p.style.left = originX + 'px';
      p.style.top = originY + 'px';
      p.style.borderRadius = Math.random() > 0.5 ? '50%' : '2px';

      const angle = Math.random() * Math.PI * 2;
      const dist = 60 + Math.random() * spread;
      const dx = Math.cos(angle) * dist;
      const dy = Math.sin(angle) * dist - 60;
      const rot = Math.random() * 720 - 360;

      p.animate([
        { transform: 'translate(0,0) rotate(0deg)', opacity: 1 },
        { transform: `translate(${dx}px, ${dy + 260}px) rotate(${rot}deg)`, opacity: 0 }
      ], { duration: 1300 + Math.random() * 700, easing: 'cubic-bezier(.2,.8,.2,1)' });

      document.body.appendChild(p);
      setTimeout(() => p.remove(), 2200);
    }
  }

  // Trail stops toggle open/closed
  document.querySelectorAll('.stop').forEach(stop => {
    stop.addEventListener('click', () => stop.classList.toggle('open'));
  });

  // Balloons: tap to pop, with a little confetti puff
  document.querySelectorAll('[data-balloon]').forEach(balloon => {
    balloon.addEventListener('click', () => {
      if (balloon.classList.contains('popped')) return;
      const rect = balloon.getBoundingClientRect();
      spawnConfetti(rect.left + rect.width / 2, rect.top + rect.height / 2, 18, 140);
      balloon.classList.add('popped');
    });
  });

  // Candles: tap each flame to blow it out; when all are out, reveal the wish
  const cakeSection = document.getElementById('cakeSection');
  const cakeHint = document.getElementById('cakeHint');
  const candles = document.querySelectorAll('[data-candle]');

  candles.forEach(candle => {
    candle.addEventListener('click', () => {
      if (candle.classList.contains('blown')) return;
      candle.classList.add('blown');

      const allBlown = [...candles].every(c => c.classList.contains('blown'));
      if (allBlown) {
        cakeSection.classList.add('all-blown');
        cakeHint.style.opacity = '0';
        const rect = cakeSection.querySelector('.cake-base').getBoundingClientRect();
        spawnConfetti(rect.left + rect.width / 2, rect.top, 60, 260);
      }
    });
  });

  // Balloon pop mini-game: tap each one, track progress
  const popBalloons = document.querySelectorAll('[data-pop]');
  const popCount = document.getElementById('popCount');
  let poppedCount = 0;

  popBalloons.forEach(balloon => {
    balloon.addEventListener('click', () => {
      if (balloon.classList.contains('popped')) return;
      balloon.classList.add('popped');
      poppedCount++;
      popCount.textContent = `${poppedCount} / ${popBalloons.length} popped`;

      const rect = balloon.getBoundingClientRect();
      spawnConfetti(rect.left + rect.width / 2, rect.top + rect.height / 2, 14, 110);

      if (poppedCount === popBalloons.length) {
        popCount.textContent = `All popped! Lucky year ahead 🍀`;
      }
    });
  });

  // Hearts boom: tap the heart button to send hearts floating up the screen
  const heartButton = document.getElementById('heartButton');
  const heartEmojis = ['💗','💖','💕','💞','❤️'];

  heartButton.addEventListener('click', () => {
    const rect = heartButton.getBoundingClientRect();
    const originX = rect.left + rect.width / 2;
    const originY = rect.top;

    for (let i = 0; i < 24; i++) {
      const h = document.createElement('div');
      h.className = 'heart-piece';
      h.textContent = heartEmojis[Math.floor(Math.random() * heartEmojis.length)];
      h.style.left = (originX + (Math.random() * 160 - 80)) + 'px';
      h.style.top = originY + 'px';
      h.style.fontSize = (1 + Math.random() * 1.4) + 'rem';

      const drift = Math.random() * 120 - 60;
      const riseHeight = window.innerHeight * (0.6 + Math.random() * 0.4);
      const rot = Math.random() * 60 - 30;

      h.animate([
        { transform: 'translate(0,0) rotate(0deg)', opacity: 1 },
        { transform: `translate(${drift}px, -${riseHeight}px) rotate(${rot}deg)`, opacity: 0 }
      ], { duration: 1800 + Math.random() * 900, easing: 'ease-out' });

      document.body.appendChild(h);
      setTimeout(() => h.remove(), 2800);
    }
  });

  // Photo gallery: tap to flip each card
  document.querySelectorAll('[data-flip]').forEach(card => {
    card.addEventListener('click', () => card.classList.toggle('flipped'));
  });

  // Envelope: tap to open, revealing the letter
  const envelope = document.getElementById('envelope');
  const letterSection = document.getElementById('letterSection');
  const letterHint = document.getElementById('letterHint');

  envelope.addEventListener('click', () => {
    const isOpen = envelope.classList.toggle('open');
    letterSection.classList.toggle('open', isOpen);
    letterHint.style.opacity = isOpen ? '0' : '0.55';
  });

  // Treasure chest -> confetti burst + wish reveal
  const chest = document.getElementById('chest');
  const treasure = document.getElementById('treasure');
  const chestHint = document.getElementById('chestHint');
  let opened = false;

  chest.addEventListener('click', () => {
    if (opened) return;
    opened = true;
    chest.textContent = '💎';
    chest.classList.add('opened');
    treasure.classList.add('opened');
    chestHint.style.opacity = '0';

    const rect = chest.getBoundingClientRect();
    spawnConfetti(rect.left + rect.width / 2, rect.top, 60, 260);
  });
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        PAGE,
        name=NAME,
        age_label=AGE_LABEL,
        final_wish=FINAL_WISH,
        photo1=url_for('static', filename='images/photo1.jpg'),
        photo2=url_for('static', filename='images/photo2.jpg'),
        photo3=url_for('static', filename='images/photo3.jpg'),
        photo4=url_for('static', filename='images/photo4.jpg'),
    )

if __name__ == "__main__":
    app.run(debug=True)