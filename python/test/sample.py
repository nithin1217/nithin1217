import re



def extractQuestion(con):
    reg_str = '<p>(.*)</p>'
    res = re.findall(reg_str, con)
    return res[0]

def extractOptions(con):
    reg_str = '(?<=<span>)([\w|\d|\n|\s]*)(?=<\/span>)'
    res = re.findall(reg_str, con)
    return res  

def extractSection(con):
    reg_str = '<section>(\s.*\s.*\s.*)</section>'
    return re.findall(reg_str, con)[0]


s = """<html lang="en"><head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Awesome Quiz App | CodingNepal</title>
    <link rel="stylesheet" href="style.css">
    <!-- FontAweome CDN Link for Icons-->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
</head>
<body>
    <!-- start Quiz button -->
    <div class="start_btn"><button name="n" id="1">Start Quiz</button></div>

    <!-- Info Box -->
    <div class="info_box">

        <div class="buttons">
            <button class="quit">Exit Quiz</button>
            <button class="restart">Continue</button>
        </div>
    </div>

    <!-- Quiz Box -->
    <div class="quiz_box activeQuiz">
        <header>
            <div class="title">Awesome Quiz Application</div>
            <div class="timer">
                <div class="time_left_txt">Time Left</div>
                <div class="timer_sec">60</div>
            </div>
            <div class="time_line" style="width: 1px;"></div>
        </header>
        <section>
            <div class="que_text"><p>1. What does HTML stand for?</p></div>
            <div class="option_list"><div class="option" onclick="optionSelected(this)"><span>Hyper Text Preprocessor</span></div><div class="option" onclick="optionSelected(this)"><span>Hyper Text Markup Language</span></div><div class="option" onclick="optionSelected(this)"><span>Hyper Text Multiple Language</span></div><div class="option" onclick="optionSelected(this)"><span>Hyper Tool Multi Language</span></div></div>    
        </section>

        <!-- footer of Quiz Box -->
        <footer>
            <div class="total_que"><span><p>1</p> of <p>5</p> Questions</span></div>
            <button class="next_btn">Next Que</button>
        </footer>
    </div>

    <!-- Result Box -->
    <div class="result_box">
        <div class="icon">
            <i class="fas fa-crown"></i>
        </div>
        <div class="complete_text">You've completed the Quiz!</div>
        <div class="score_text">
            <!-- Here I've inserted Score Result from JavaScript -->
        </div>
        <div class="buttons">
            <button class="restart">Replay Quiz</button>
            <button class="quit">Quit Quiz</button>
        </div>
    </div>

    <!-- Inside this JavaScript file I've inserted Questions and Options only -->
    <script src="js/questions.js"></script>

    <!-- Inside this JavaScript file I've coded all Quiz Codes -->
    <script src="js/script.js"></script>


</body></html>"""

section = extractSection(s)[0]
section = str(section).strip()
print(extractOptions(section))