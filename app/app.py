import random
import streamlit as st

st.set_page_config(page_title="AI-Based Personalized Learning System")
st.title("📘 AI-Based Personalized Learning System")
st.write("Practice quizzes, check your answers, and get topic-wise revision advice.")
st.info("Free version: uses built-in questions. No OpenAI API key, credits, or database required.")

BANK = {
"Python": {
"Variables": [
("Which symbol assigns a value in Python?", ["==", "=", "!=", ":"], "=", "The = symbol assigns a value."),
("What is the type of 2.5?", ["int", "float", "str", "bool"], "float", "A decimal number is a float."),
("Which is a valid variable name?", ["2score", "total-score", "total_score", "class"], "total_score", "Names cannot start with digits, contain hyphens, or use keywords."),
("What does x += 2 do?", ["Subtracts 2", "Adds 2 to x", "Sets x to 2", "Compares x"], "Adds 2 to x", "It is shorthand for x = x + 2.")],
"Conditions": [
("Which keyword checks another condition after if?", ["else if", "elif", "then", "switch"], "elif", "Python uses elif for another condition."),
("What is the result of 4 > 2?", ["True", "False", "4", "2"], "True", "Four is greater than two."),
("What is printed by: print('yes' if 8 > 5 else 'no')?", ["yes", "no", "8", "Error"], "yes", "The condition is true."),
("What is (True and False) or True?", ["True", "False", "None", "Error"], "True", "False or True evaluates to True.")],
"Loops": [
("Which loop can iterate over a list?", ["for", "switch", "case", "goto"], "for", "A for loop iterates through an iterable."),
("How many values are in range(3)?", ["2", "3", "4", "1"], "3", "range(3) produces 0, 1, 2."),
("What does break do in a loop?", ["Skips one iteration", "Ends the loop", "Restarts it", "Defines a function"], "Ends the loop", "break exits the nearest loop."),
("What does continue do?", ["Ends the program", "Skips to the next iteration", "Deletes the loop", "Returns a value"], "Skips to the next iteration", "continue skips the rest of the current iteration.")],
"Functions": [
("Which keyword defines a Python function?", ["func", "def", "function", "make"], "def", "Function definitions begin with def."),
("Which statement sends a result back?", ["print", "return", "break", "input"], "return", "return gives a value back to the caller."),
("What does add(2,3) return if add returns a+b?", ["23", "5", "None", "Error"], "5", "Two plus three is five."),
("What is a parameter used for?", ["Pass input to a function", "Stop a loop", "Print automatically", "Import a module"], "Pass input to a function", "Parameters allow functions to receive values.")],
"Lists": [
("Which brackets create a list?", ["()", "{}", "[]", "<>"], "[]", "Python lists use square brackets."),
("What is the first list index?", ["0", "1", "-1", "None"], "0", "Python indexing starts at zero."),
("What is len([4,7,9])?", ["2", "3", "4", "9"], "3", "The list contains three elements."),
("Which method adds an item to the end of a list?", ["push()", "append()", "add_end()", "put()"], "append()", "append adds an item to the end.")],
},
"Data Structures": {
"Arrays": [
("In a zero-indexed array, what is the first index?", ["0", "1", "-1", "2"], "0", "Zero-indexed arrays start at index zero."),
("What is the typical time for array index access?", ["O(1)", "O(n)", "O(log n)", "O(n²)"], "O(1)", "Direct index access takes constant time."),
("Why can inserting at an array's beginning take O(n)?", ["Elements may need shifting", "It becomes a tree", "It sorts itself", "It removes indices"], "Elements may need shifting", "Existing elements may need to move."),
("Which structure stores elements in indexed positions?", ["Array", "Stack only", "Tree only", "Graph only"], "Array", "Array elements are accessed by index.")],
"Linked Lists": [
("A singly linked-list node usually stores what?", ["Data and next pointer", "Only an index", "Two arrays", "A queue"], "Data and next pointer", "The pointer links to the next node."),
("What marks the end of a typical singly linked list?", ["NULL", "Root", "Rear", "Index 1"], "NULL", "The last node's next pointer is NULL."),
("What is typical time to search a linked list?", ["O(1)", "O(log n)", "O(n)", "O(n²)"], "O(n)", "You may need to visit each node."),
("What does a pointer in a linked list help do?", ["Connect nodes", "Sort automatically", "Store every index", "Calculate length instantly"], "Connect nodes", "Pointers or references link nodes together.")],
"Stacks": [
("Which principle does a stack follow?", ["FIFO", "LIFO", "Random", "Sorted"], "LIFO", "Last In, First Out."),
("Which operation adds an item to a stack?", ["Push", "Pop", "Dequeue", "Front"], "Push", "Push inserts at the top."),
("Which operation removes the top item?", ["Push", "Pop", "Peek", "Enqueue"], "Pop", "Pop removes the top item."),
("Which application naturally uses a stack?", ["Undo history", "Printer queue", "Level-order traversal", "Round-robin scheduling"], "Undo history", "The most recent action is undone first.")],
"Queues": [
("Which principle does a standard queue follow?", ["LIFO", "FIFO", "Random", "Sorted"], "FIFO", "First In, First Out."),
("Which operation adds an item to a queue?", ["Push", "Pop", "Enqueue", "Peek"], "Enqueue", "Enqueue adds at the rear."),
("Where is an item removed from a standard queue?", ["Rear", "Front", "Middle", "Both ends"], "Front", "Dequeue removes from the front."),
("Why use a circular queue?", ["Reuse empty positions", "Sort automatically", "Avoid all indexes", "Make it a tree"], "Reuse empty positions", "The rear can wrap around to reuse free space.")],
"Trees": [
("What is the topmost node of a tree called?", ["Leaf", "Root", "Edge", "Sibling"], "Root", "The root has no parent."),
("A node with no children is called what?", ["Root", "Leaf", "Parent", "Edge"], "Leaf", "A leaf has no children."),
("How many children can a binary-tree node have at most?", ["1", "2", "3", "Unlimited"], "2", "It can have a left child and a right child."),
("Average search time in a balanced BST is typically?", ["O(1)", "O(log n)", "O(n²)", "O(2ⁿ)"], "O(log n)", "A balanced tree has logarithmic height.")],
}
}

ALIASES = {"array":"Arrays","linked list":"Linked Lists","stack":"Stacks","queue":"Queues",
           "tree":"Trees","binary tree":"Trees","bst":"Trees","list":"Lists",
           "variable":"Variables","python basics":"Variables","condition":"Conditions",
           "if else":"Conditions","function":"Functions","loop":"Loops"}

with st.form("setup"):
    subject = st.selectbox("Subject", list(BANK))
    topics_text = st.text_input("Topics (separate with commas)", "Loops, Functions" if subject == "Python" else "Stacks, Queues")
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard", "Mixed"])
    count = st.selectbox("Questions per topic", [2, 3, 4])
    start = st.form_submit_button("Prepare quiz")

if start:
    topics, unknown = [], []
    for raw in topics_text.split(","):
        name = raw.strip()
        if not name:
            continue
        canonical = ALIASES.get(name.lower(), name)
        match = next((t for t in BANK[subject] if t.lower() == canonical.lower()), None)
        if match and match not in topics:
            topics.append(match)
        elif not match:
            unknown.append(name)
    if not topics:
        st.error("Enter at least one valid topic.")
    elif len(topics) > 5:
        st.error("Please enter no more than five topics.")
    elif unknown:
        st.error("Unknown topic(s): " + ", ".join(unknown))
        st.write("Available topics:", ", ".join(BANK[subject]))
    else:
        quiz = []
        for topic in topics:
            pool = BANK[subject][topic]
            if difficulty != "Mixed":
                # The built-in bank is mixed difficulty; keep questions available and label it honestly.
                pool = pool[:]
            chosen = random.sample(pool, min(count, len(pool)))
            for q in chosen:
                quiz.append({"topic": topic, "question": q[0], "options": q[1], "answer": q[2], "explanation": q[3]})
        random.shuffle(quiz)
        st.session_state.quiz = quiz
        st.session_state.quiz_topics = topics
        st.session_state.answers = {}
        st.session_state.finished = False

if "quiz" in st.session_state and not st.session_state.get("finished", False):
    st.divider()
    st.header("Your quiz")
    with st.form("quiz_answer_form"):
        answers = {}
        for i, q in enumerate(st.session_state.quiz, 1):
            st.markdown(f"**Q{i}. [{q['topic']}] {q['question']}**")
            answers[str(i)] = st.radio("Select an answer", q["options"], index=None, key=f"q_{i}")
        submit = st.form_submit_button("Submit answers")
    if submit:
        st.session_state.answers = answers
        st.session_state.finished = True
        st.rerun()

if st.session_state.get("finished", False):
    st.divider()
    st.header("Your results")
    quiz = st.session_state.quiz
    answers = st.session_state.answers
    stats = {t: [0, 0] for t in st.session_state.quiz_topics}
    correct_total = 0
    for i, q in enumerate(quiz, 1):
        stats[q["topic"]][1] += 1
        if answers.get(str(i)) == q["answer"]:
            stats[q["topic"]][0] += 1
            correct_total += 1
    total = len(quiz)
    overall = round(100 * correct_total / total) if total else 0
    st.metric("Overall score", f"{overall}%", f"{correct_total}/{total} correct")
    st.subheader("Topic-wise performance")
    for topic, (right, total_topic) in stats.items():
        pct = round(100 * right / total_topic)
        st.write(f"**{topic}: {pct}% ({right}/{total_topic})**")
        st.progress(pct / 100)
        if pct >= 70:
            st.success("Strong — try harder questions next.")
        elif pct >= 50:
            st.warning("Developing — review the topic and practise again.")
        else:
            st.error("Needs revision — revisit the basics, then retry.")
    st.subheader("Answer review")
    for i, q in enumerate(quiz, 1):
        ok = answers.get(str(i)) == q["answer"]
        st.markdown(f"**Q{i}. {q['question']}**")
        st.write("Your answer:", answers.get(str(i)) or "Not answered")
        st.write("Correct answer:", q["answer"])
        st.write("Explanation:", q["explanation"])
        st.write("Correct ✅" if ok else "Incorrect ❌")
    st.caption("Questions are predefined. Scores and recommendations are calculated by Python rules. This short quiz is for practice, not a complete measure of ability.")
    if st.button("Start another quiz"):
        for key in ["quiz", "quiz_topics", "answers", "finished"]:
            st.session_state.pop(key, None)
        st.rerun()

st.sidebar.header("Available topics")
st.sidebar.write("**Python:** " + ", ".join(BANK["Python"]))
st.sidebar.write("**Data Structures:** " + ", ".join(BANK["Data Structures"]))
st.sidebar.caption("No API key, database, or payment required.")
