# from flask import Flask, render_template_string

# app = Flask(__name__)

# HTML = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
# <meta charset="UTF-8">
# <title>Happy Birthday!</title>

# <script src="https://cdn.tailwindcss.com"></script>
# <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.3/dist/confetti.browser.min.js"></script>

# <style>

# body{
# margin:0;
# font-family:Arial,Helvetica,sans-serif;
# background:linear-gradient(135deg,#ffe6f2,#fff5e6,#ffffff);
# overflow-x:hidden;
# text-align:center;
# }

# h1{
# font-size:3rem;
# color:#ff4d88;
# margin-top:30px;
# }

# .subtitle{
# color:#666;
# font-size:18px;
# margin-bottom:40px;
# }

# #giftSection{
# margin-top:20px;
# }

# .gift{
# width:170px;
# height:150px;
# margin:auto;
# position:relative;
# cursor:pointer;
# transition:.5s;
# }

# .box{
# position:absolute;
# bottom:0;
# width:170px;
# height:100px;
# background:#ff5fa2;
# border-radius:8px;
# }

# .ribbonV{
# position:absolute;
# left:76px;
# width:18px;
# height:100px;
# background:gold;
# }

# .ribbonH{
# position:absolute;
# top:40px;
# width:170px;
# height:18px;
# background:gold;
# }

# .lid{
# position:absolute;
# top:0;
# width:180px;
# height:45px;
# left:-5px;
# background:#ff78b4;
# border-radius:8px;
# transition:1s;
# transform-origin:left bottom;
# }

# .open .lid{
# transform:rotate(-35deg) translate(-20px,-25px);
# }

# .hiddenSection{
# display:none;
# animation:fadeIn 1.5s;
# }

# @keyframes fadeIn{
# from{opacity:0;transform:translateY(20px);}
# to{opacity:1;transform:translateY(0);}
# }

# .cake{
# margin:50px auto;
# position:relative;
# width:220px;
# height:180px;
# }

# .layer1{
# position:absolute;
# bottom:0;
# width:220px;
# height:90px;
# background:#ff9ecb;
# border-radius:10px;
# }

# .layer2{
# position:absolute;
# bottom:80px;
# left:20px;
# width:180px;
# height:60px;
# background:#ffc2dd;
# border-radius:10px;
# }

# .candle{
# position:absolute;
# width:10px;
# height:45px;
# background:white;
# top:25px;
# }

# .flame{
# position:absolute;
# width:14px;
# height:18px;
# background:gold;
# border-radius:50%;
# top:-18px;
# left:-2px;
# animation:flicker .3s infinite alternate;
# box-shadow:0 0 15px gold;
# }

# @keyframes flicker{
# from{transform:scale(1);}
# to{transform:scale(.8);}
# }

# .card{
# width:80%;
# max-width:600px;
# margin:40px auto;
# background:white;
# padding:25px;
# border-radius:20px;
# box-shadow:0 10px 30px rgba(0,0,0,.1);
# }

# button{
# padding:14px 28px;
# font-size:18px;
# border:none;
# border-radius:40px;
# background:#ff4d88;
# color:white;
# cursor:pointer;
# margin:15px;
# transition:.3s;
# }

# button:hover{
# background:#ff1f6b;
# transform:scale(1.05);
# }

# </style>
# </head>

# <body>

# <h1>🎉 Happy Birthday, My Babe My Utkarsh Sharma 🎉</h1>

# <p class="subtitle">
# Click the gift to begin your surprise!
# </p>

# <div id="giftSection">

# <div class="gift" id="gift" onclick="openGift()">

# <div class="lid"></div>

# <div class="box">
# <div class="ribbonV"></div>
# <div class="ribbonH"></div>
# </div>

# </div>

# </div>

# <div id="birthdayContent" class="hiddenSection">

# <div class="cake">

# <div class="layer1"></div>

# <div class="layer2"></div>

# <div class="candle" style="left:60px;">
# <div class="flame"></div>
# </div>

# <div class="candle" style="left:105px;">
# <div class="flame"></div>
# </div>

# <div class="candle" style="left:150px;">
# <div class="flame"></div>
# </div>

# </div>

# <button onclick="blowCandles()">
# 🕯 Blow Out Candles
# </button>

# <button onclick="celebrate()">
# 🎂 Cut the Cake
# </button>

# <div class="card">

# <h2>💌 A Special Birthday Message For My Cute Hubby 💌</h2>

# <p style="font-size:18px;color:#555;line-height:1.8;">

# Dear <b>Utkarsh sharma</b>,<br><br>

# Wishing you a birthday filled with laughter,
# love, happiness, and unforgettable memories.

# May every dream you have come true,
# and may this year bring endless success,
# good health, and beautiful moments.

# Thank you for being such an Cute Hubby.

# 🎉 Happy Birthday Mere Jannn! 🎉

# </p>

# </div>

# </div>

# <script>

# function openGift(){

# document.getElementById("gift").classList.add("open");

# setTimeout(function(){

# document.getElementById("birthdayContent").style.display="block";

# celebrate();

# },900);

# }

# function celebrate(){

# confetti({
# particleCount:180,
# spread:180,
# origin:{y:.6}
# });

# }

# function blowCandles(){

# let flames=document.querySelectorAll(".flame");

# flames.forEach(f=>{

# f.style.display="none";

# });

# confetti({
# particleCount:120,
# spread:120
# });

# }

# </script>

# </body>
# </html>
# """

# @app.route("/")
# def home():
#     return render_template_string(HTML)

# if __name__ == "__main__":
#     app.run(debug=True)









import streamlit as st
from datetime import datetime
import time

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------

st.set_page_config(
    page_title="Happy Birthday",
    page_icon="🎂",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#ffdde1,#fceabb);
}

h1{
text-align:center;
color:#6A1B9A;
font-size:60px;
}

.big{
font-size:28px;
text-align:center;
color:#444;
}

.card{

background:white;
padding:30px;
border-radius:20px;
box-shadow:0px 10px 25px rgba(0,0,0,0.2);
color:#C2185B;
}

.count{

font-size:35px;
font-weight:bold;
text-align:center;
color:#D4AF37;

}
.surprise-card{

background:Deep Pink;
padding:30px;
border-radius:20px;
margin-top:20px;
box-shadow:0 10px 25px rgba(0,0,0,.25);

animation:popup .6s ease;

}

@keyframes popup{

0%{
transform:scale(.5);
opacity:0;
}

100%{
transform:scale(1);
opacity:1;
}

}

button[kind="primary"]{

background:#ff1493;
color:Red;
border-radius:12px;

}.surprise-card{

background:blue;
padding:30px;
border-radius:20px;
margin-top:20px;
box-shadow:0 10px 25px rgba(0,0,0,.25);

animation:popup .6s ease;

}

@keyframes popup{

0%{
transform:scale(.5);
opacity:0;
}

100%{
transform:scale(1);
opacity:1;
}

}

button[kind="primary"]{

background:#ff1493;
color:Purple;
border-radius:12px;

}

</style>
""",unsafe_allow_html=True)

# -----------------------------
# CUSTOMIZE HERE
# -----------------------------

NAME="Friend ❤️"

# Birthday

birthday=datetime(2026,12,25,0,0,0)

# -----------------------------
# TITLE
# -----------------------------

st.markdown(f"<h1>🎉 Happy Birthday {NAME}! 🎉</h1>",unsafe_allow_html=True)

st.markdown(
"<p class='big'>Counting down to your special day ❤️</p>",
unsafe_allow_html=True
)

st.divider()

# -----------------------------
# LIVE COUNTDOWN
# -----------------------------

st.markdown("## ⏳ Countdown")

placeholder = st.empty()

now = datetime.now()

remaining = birthday - now

if remaining.total_seconds() > 0:

    days = remaining.days

    hours = remaining.seconds // 3600

    minutes = (remaining.seconds % 3600) // 60

    seconds = remaining.seconds % 60

    placeholder.markdown(
        f"""
        <div class="count">
            {days} Days
            <br>
            {hours} Hours
            <br>
            {minutes} Minutes
            <br>
            {seconds} Seconds
        </div>
        """,
        unsafe_allow_html=True
    )

else:

    st.success("🎉 Happy Birthday! 🎂❤️")

# -----------------------------
# MESSAGE CARD
# -----------------------------

st.markdown("## 💌 A Special Message")

st.markdown("""

<div class="card">

Dear <b>Babe ❤️</b>

<br><br>

Every moment spent with you
is a beautiful memory.

May your birthday be filled
with endless happiness,
love,
success,
smiles,
and unforgettable memories.

You deserve all the happiness
in the world.

Happy Birthday! ❤️

</div>

""",unsafe_allow_html=True)

st.write("")

# -----------------------------
# IMAGE PLACEHOLDER
# -----------------------------

st.markdown("## 📸 Beautiful Memory")

st.image(

"https://via.placeholder.com/900x500.png?text=Your+Favorite+Photo",

use_container_width=True

)

st.write("")
# ==========================================================
# 🎁 SURPRISE SECTION
# ==========================================================

st.divider()

st.markdown(
    """
    <h2 style="text-align:center;
               color:#ff1493;
               font-size:40px;">
        🎁 Special Birthday Surprise 🎁
    </h2>
    """,
    unsafe_allow_html=True
)

st.write("")

st.markdown(
    """
    <div style="
        background:white;
        padding:25px;
        border-radius:20px;
        box-shadow:0px 10px 25px rgba(0,0,0,0.20);
        text-align:center;
    ">

    <h3 style="color:#ff1493;">
        Ready for your surprise? ❤️
    </h3>

    <p style="font-size:20px;color:#333333;">
        Click the button below and unlock
        your birthday surprise!
    </p>

    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ==========================================================
# SURPRISE BUTTON
# ==========================================================

if st.button("🎉 Click For A Surprise!", use_container_width=True):

    # Balloons Animation
    st.balloons()

    # Snow Animation
    st.snow()

    # Success Message
    st.success("🎉 Surprise Unlocked Successfully!")

    st.write("")

    # Hidden Birthday Card
    st.markdown(
        """
        <div style="
            background:white;
            padding:35px;
            border-radius:20px;
            box-shadow:0px 10px 25px rgba(0,0,0,0.25);
        ">

        <h1 style="
            color:#ff1493;
            text-align:center;">
            💖 Happy Birthday Babe 💖
        </h1>

        <hr>

        <p style="
            font-size:22px;
            color:#5D4037;
            text-align:center;
            line-height:2;
        ">

        Wishing you a day filled with
        happiness ❤️

        laughter 😊

        love 💕

        success 🌸

        beautiful memories 📸

        and endless smiles ✨

        <br><br>

        Thank you for being such an amazing
        person.

        <br><br>

        May all your dreams come true.

        <br><br>

        ❤️ Happy Birthday Once Again ❤️

        </p>

        </div>

        """,
        unsafe_allow_html=True
    )

    st.write("")

    # Birthday Statistics

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🎂 Cakes",
            "1"
        )

    with col2:
        st.metric(
            "🎁 Gifts",
            "∞"
        )

    with col3:
        st.metric(
            "❤️ Love",
            "Unlimited"
        )

    st.write("")

    st.info("✨ More surprises are waiting...")

st.info("✨ Part 1 Completed Successfully!")

# ==========================================
# SURPRISE SECTION
# ==========================================

st.divider()

st.markdown(
"""
<h2 style='text-align:center;color:#ff1493;'>

🎁 Birthday Surprise 🎁

</h2>
""",
unsafe_allow_html=True
)

st.write("")

surprise = st.button(
    "🎉 Click For A Surprise!",
    use_container_width=True,
    key="surprise_button"
    
)

if surprise:

    st.balloons()

    st.snow()

    st.success("🎉 Surprise Unlocked!")

    st.markdown(
    """

    <div class='surprise-card'>

    <h2 style='text-align:center;color:#6A1B9A;'>

    💖 Happy Birthday Babe 💖

    </h2>

    <hr>

    <p style='font-size:22px;text-align:center;'>

    Today is your special day.

    I hope your life is always filled with

    happiness,

    love,

    laughter,

    success,

    beautiful memories,

    and endless smiles.

    <br><br>

    Never stop smiling because your smile

    makes the world brighter.

    <br><br>

    ❤️

    Happy Birthday Once Again

    ❤️

    </p>

    </div>

    """,
    unsafe_allow_html=True
    )

    st.write("")

    col1,col2,col3=st.columns(3)

    with col1:

        st.metric(

        "🎂 Cakes",

        "1"

        )

    with col2:

        st.metric(

        "🎁 Gifts",

        "∞"

        )

    with col3:

        st.metric(

        "❤️ Love",

        "Unlimited"

        )

    st.info("✨ More surprises are coming...")

# ==========================================================
# 🔒 SECRET GIFT + 🎉 BIRTHDAY JOURNEY
# ==========================================================

st.write("")
st.divider()

# -------------------------------
# Secret Gift Locked
# -------------------------------

st.markdown(
"""
<div style="
background:linear-gradient(135deg,#ffd6e8,#fff8dc);
padding:35px;
border-radius:25px;
text-align:center;
box-shadow:0px 10px 25px rgba(0,0,0,0.25);
margin-bottom:30px;
">

<h1 style="color:#ff1493;">
🔒 Secret Gift Locked 🔒
</h1>

<p style="
font-size:22px;
color:#444444;
line-height:2;
">

Congratulations Babe ❤️

You have successfully unlocked
the first birthday surprise.

But wait...

A mysterious gift is still waiting
just for you. 🎁

Keep scrolling to continue your
Birthday Adventure...

👇👇👇

</p>

</div>
""",
unsafe_allow_html=True
)

# -------------------------------
# Birthday Journey
# -------------------------------

st.markdown(
"""
<div style="
background:linear-gradient(135deg,#ff9ec4,#ffd700);
padding:35px;
border-radius:25px;
text-align:center;
box-shadow:0px 10px 25px rgba(0,0,0,0.25);
">

<h1 style="color:white;">
🎉 Birthday Journey 🎉
</h1>

<h2 style="color:white;">
Level 1 Completed ✅
</h2>

<hr>

<p style="
font-size:22px;
color:white;
line-height:2;
">

Your Birthday Adventure
Has Just Begun...

✨ Upcoming Surprises ✨

🎂 Premium Birthday Cake

🕯️ Blow Out The Candles

💌 Secret Love Letter

🎁 Final Birthday Surprise

❤️ A Special Ending

</p>

</div>
""",
unsafe_allow_html=True
)

st.write("")

# Progress Bar

st.markdown("### 🎯 Birthday Progress")

st.progress(25)

st.success("✨ You have completed 25% of the Birthday Adventure!")

# ==========================================================
# 🎂 PREMIUM BIRTHDAY CAKE
# ==========================================================

st.write("")
st.divider()

st.markdown(
"""
<h1 style="
text-align:center;
color:#ff1493;
font-size:50px;
">
🎂 Premium Birthday Cake 🎂
</h1>

<p style="
text-align:center;
font-size:24px;
color:#222222;
">
A delicious cake made especially for you ❤️
</p>
""",
unsafe_allow_html=True
)

# -----------------------------
# Cake Card
# -----------------------------

st.markdown(
"""
<div style="
background:white;
padding:40px;
border-radius:30px;
box-shadow:0px 10px 30px rgba(0,0,0,0.20);
margin-top:20px;
text-align:center;
">

<div style="font-size:60px;">
✨
🕯️ &nbsp;&nbsp; 🕯️ &nbsp;&nbsp; 🕯️
</div>

<div style="font-size:200px;line-height:1;">
🎂
</div>

<h2 style="color:#ff1493;">
Happy Birthday Babe ❤️
</h2>

<p style="
font-size:20px;
color:#444444;
line-height:1.8;
">

This cake is baked with

❤️ Love

😊 Happiness

🌸 Beautiful Memories

✨ Sweet Moments

🎁 Endless Smiles

Especially for You.

</p>

</div>
""",
unsafe_allow_html=True
)

st.write("")
st.info("👇 Scroll Down to Blow Out the Candles 💨")

# ==========================================================
# 💨 BLOW OUT THE CANDLES
# ==========================================================

# Session State
if "candles_blown" not in st.session_state:
    st.session_state.candles_blown = False

st.write("")

# -----------------------------
# Candles Still Burning
# -----------------------------
if not st.session_state.candles_blown:

    st.markdown(
    """
    <div style="
    background:#fff;
    padding:30px;
    border-radius:25px;
    text-align:center;
    box-shadow:0px 10px 25px rgba(0,0,0,.2);
    ">

    <h2 style="color:#ff1493;">
    🕯️ The Candles Are Still Glowing 🕯️
    </h2>

    <div style="font-size:70px;">
    🔥🕯️ &nbsp; 🔥🕯️ &nbsp; 🔥🕯️
    </div>

    <p style="
    font-size:22px;
    color:#444;
    ">

    Make a wish...

    Then click the button below
    to blow out the candles.

    </p>

    </div>
    """,
    unsafe_allow_html=True
    )

    st.write("")

    if st.button(
        "💨 Blow Out the Candles",
        use_container_width=True,
        key="blow_candles"
    ):

        st.session_state.candles_blown = True

        st.balloons()

        st.snow()

        st.rerun()

# -----------------------------
# Candles Blown
# -----------------------------
else:

    st.markdown(
    """
    <div style="
    background:white;
    padding:35px;
    border-radius:25px;
    text-align:center;
    box-shadow:0px 10px 25px rgba(0,0,0,.25);
    ">

    <h1 style="color:#ff1493;">
    🎉 Wonderful! 🎉
    </h1>

    <div style="font-size:70px;">
    💨🕯️ &nbsp; 💨🕯️ &nbsp; 💨🕯️
    </div>

    <h2 style="color:#e91e63;">
    You Blew Out All The Candles ❤️
    </h2>

    <p style="
    font-size:22px;
    color:#444;
    line-height:2;
    ">

    Your birthday wish
    has been sent to the stars ⭐

    May all your dreams
    come true.

    Happy Birthday Babe ❤️

    </p>

    </div>
    """,
    unsafe_allow_html=True
    )

    st.success("✨ Don't tell anyone what you wished for... It might come true! 🤫")

    st.progress(50)

    st.info("🎁 50% Birthday Journey Completed!")

# ==========================================================
# 💌 SECRET LOVE LETTER
# ==========================================================

st.write("")
st.divider()

st.markdown("""
<h1 style="
text-align:center;
color:#ff1493;
font-size:50px;
">
💌 Secret Love Letter 💌
</h1>

<p style="
text-align:center;
font-size:22px;
color:#555;
">
A special letter is waiting just for you ❤️
</p>
""", unsafe_allow_html=True)

st.write("")

# ------------------------------------
# Session State
# ------------------------------------

if "letter_opened" not in st.session_state:
    st.session_state.letter_opened = False

# ------------------------------------
# Closed Envelope
# ------------------------------------

if not st.session_state.letter_opened:

    st.markdown("""
    <div style="
    background:white;
    padding:40px;
    border-radius:25px;
    text-align:center;
    box-shadow:0px 10px 25px rgba(0,0,0,.2);
    ">

    <div style="font-size:120px;">
    ✉️
    </div>

    <h2 style="color:#ff1493;">
    A Letter Just For You ❤️
    </h2>

    <p style="
    font-size:20px;
    color:#555;
    ">

    Someone wrote something
    special for you...

    Open it to read.

    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button(
        "💌 Open My Letter",
        use_container_width=True,
        key="love_letter"
    ):

        st.session_state.letter_opened = True

        st.balloons()

        st.rerun()

# ------------------------------------
# Open Letter
# ------------------------------------

else:

    st.markdown("""
    <div style="
    background:white;
    padding:40px;
    border-radius:25px;
    box-shadow:0px 10px 25px rgba(0,0,0,.25);
    ">

    <h1 style="
    text-align:center;
    color:#6A0DAD;
    ">
    ❤️ Dear Babe ❤️
    </h1>

    <hr>

    <p style="
    font-size:22px;
    color:#444;
    line-height:2;
    ">

    Today is not just another day...

    It is the day when someone truly special
    came into this world.

    🌸

    I hope your life is always filled with

    happiness,

    success,

    endless smiles,

    unforgettable memories,

    and people who truly care about you.

    ❤️

    Keep shining.

    Keep smiling.

    Keep believing in yourself.

    Because you deserve every beautiful thing
    this world has to offer.

    🎂

    Happy Birthday Babe ❤️

    Wishing you a lifetime of love,
    laughter,
    and dreams that come true.

    </p>

    <hr>

    <h2 style="
    text-align:right;
    color:#C2185B;
    ">
    With Lots of Love ❤️
    </h2>

    </div>
    """, unsafe_allow_html=True)

    st.success("💖 Love Letter Opened Successfully!")

    st.progress(75)

    st.info("🎉 75% Birthday Journey Completed!")

# ==========================================================
# 🎁 FINAL SURPRISE
# ==========================================================

st.write("")
st.divider()

st.markdown("""
<h1 style="
text-align:center;
color:#800020;
font-size:50px;
">
🎁 Final Birthday Surprise 🎁
</h1>

<p style="
text-align:center;
font-size:22px;
color:#555;
">
One last surprise is waiting for you... ❤️
</p>
""", unsafe_allow_html=True)

# -----------------------------------
# Session State
# -----------------------------------

if "final_surprise" not in st.session_state:
    st.session_state.final_surprise = False

# -----------------------------------
# Gift Box
# -----------------------------------

if not st.session_state.final_surprise:

    st.markdown("""
    <div style="
    background:white;
    padding:40px;
    border-radius:25px;
    text-align:center;
    box-shadow:0px 10px 25px rgba(0,0,0,.25);
    ">

    <div style="font-size:120px;">
    🎁
    </div>

    <h2 style="color:#D4AF37;">
    Your Final Gift
    </h2>

    <p style="
    font-size:22px;
    color:#444;
    ">

    Thank you for completing
    this Birthday Journey.

    One final surprise
    is waiting inside this gift.

    </p>

    </div>

    """, unsafe_allow_html=True)

    st.write("")

    if st.button(
        "🎁 Open My Final Gift",
        use_container_width=True,
        key="gift_box"
    ):

        st.session_state.final_surprise = True

        st.balloons()

        st.snow()

        st.rerun()

# -----------------------------------
# Final Gift Opened
# -----------------------------------

else:

    st.balloons()
    st.snow()

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#ff9ec4,#ffe5b4);
    padding:40px;
    border-radius:30px;
    text-align:center;
    box-shadow:0px 10px 30px rgba(0,0,0,.25);
    ">

   <h1 style="
color:#C2185B;
font-size:50px;
font-weight:bold;
text-shadow:2px 2px 8px rgba(255,255,255,0.6);
">
    🎉 Congratulations 🎉
    </h1>

    <h2 style="color:Purple;">
    Happy Birthday Babe ❤️
    </h2>

    <hr>

    <p style="
color:#222222;
font-size:22px;
line-height:1.8;
">

    Thank you for visiting
    this little birthday surprise.

    I hope it made you smile.

    May your life always be filled with

    ❤️ Love

    😊 Happiness

    🌸 Beautiful Memories

    ✨ Success

    🎁 Wonderful Adventures

    🌈 Endless Smiles

    <br><br>

    You truly deserve
    all the happiness
    in the world.

    <br><br>

    ❤️ Happy Birthday Once Again ❤️

    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.success("🏆 Birthday Adventure Completed Successfully!")

    st.progress(100)

    st.markdown("""
    <h2 style="
    text-align:center;
    color:#ff1493;
    ">
    🏆 100% Completed 🏆
    </h2>
    """, unsafe_allow_html=True)

    st.info("✨ Thank you for celebrating this special day! ❤️")

st.divider()
 
st.markdown("""
<div style="
text-align:center;
padding:30px;
">

<h2 style="color:#ff1493;">
Made with ❤️ Especially For You
</h2>

<p style="
font-size:18px;
color:#555;
">

Thank you for visiting
this birthday website.

I hope it brought
a smile to your face.

🎂❤️🎁

</p>

</div>
""", unsafe_allow_html=True)