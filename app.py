import streamlit as st

# Page configuration
st.set_page_config(
    page_title="SkillSync",
    page_icon="🎯",
    layout="wide"
)

# Title
st.title("🎯 SkillSync")
st.write("Your personal skill and career development platform.")

# Sidebar
st.sidebar.header("👤 Your Profile")

name = st.sidebar.text_input("Name")
course = st.sidebar.text_input("Course")
year = st.sidebar.selectbox(
    "Year of Study",
    ["1st Year", "2nd Year", "3rd Year", "4th Year"]
)

# Main section
st.header("📋 Profile")

if name and course:
    st.success(f"Welcome, {name}! 🎉")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Course:**", course)

    with col2:
        st.write("**Year:**", year)

else:
    st.info("👈 Enter your details in the sidebar to get started.")
# Skills Section
st.divider()

st.header("💻 Your Skills")

skill = st.text_input(
    "Enter a skill you have",
    placeholder="Example: Python"
)

skill_level = st.selectbox(
    "Select your skill level",
    ["Beginner", "Intermediate", "Advanced"]
)

if skill:
    st.success(
        f"Skill added: {skill} — Level: {skill_level}"
    )
# Multiple Skills Section
st.divider()

st.header("📚 Add Multiple Skills")

skills = st.multiselect(
    "Select your skills",
    [
        "Python",
        "Java",
        "C",
        "C++",
        "HTML",
        "CSS",
        "JavaScript",
        "SQL",
        "Git",
        "Machine Learning",
        "Data Structures",
        "Problem Solving"
    ]
)

if skills:
    st.write("### Your Selected Skills")

    for selected_skill in skills:
        st.write(f"✅ {selected_skill}")
# Skill Gap Analysis
st.divider()

st.header("📊 Skill Gap Analysis")

target_role = st.selectbox(
    "Select your target career role",
    [
        "Software Developer",
        "Data Scientist",
        "Machine Learning Engineer",
        "Web Developer",
        "Data Analyst"
    ]
)

required_skills = {
    "Software Developer": [
        "Python", "Java", "Data Structures",
        "Problem Solving", "SQL", "Git"
    ],

    "Data Scientist": [
        "Python", "SQL", "Machine Learning",
        "Statistics", "Data Analysis"
    ],

    "Machine Learning Engineer": [
        "Python", "Machine Learning",
        "Data Structures", "SQL", "Problem Solving"
    ],

    "Web Developer": [
        "HTML", "CSS", "JavaScript",
        "SQL", "Git"
    ],

    "Data Analyst": [
        "Python", "SQL", "Data Analysis",
        "Statistics"
    ]
}

if skills:
    required = required_skills[target_role]

    matched_skills = [
        skill for skill in required
        if skill in skills
    ]

    missing_skills = [
        skill for skill in required
        if skill not in skills
    ]

    st.subheader("✅ Skills You Have")

    if matched_skills:
        for skill in matched_skills:
            st.write(f"✅ {skill}")
    else:
        st.write("No matching skills yet.")

    st.subheader("📌 Skills You Need to Learn")

    if missing_skills:
        for skill in missing_skills:
            st.write(f"🔴 {skill}")
    else:
        st.success("🎉 You have all the required skills!")

else:
    st.info("Please select your skills above to see your skill gap.")
# Skill Recommendations
st.divider()

st.header("🎯 Recommended Skills")

skill_recommendations = {
    "Python": "Learn Python fundamentals, functions, OOP, and libraries.",
    "Java": "Learn Java basics, OOP, collections, and exception handling.",
    "C": "Learn C fundamentals, pointers, arrays, and memory management.",
    "C++": "Learn C++ syntax, OOP, STL, and problem solving.",
    "HTML": "Learn HTML structure, forms, semantic elements, and accessibility.",
    "CSS": "Learn CSS layouts, Flexbox, Grid, and responsive design.",
    "JavaScript": "Learn JavaScript fundamentals, DOM, events, and asynchronous programming.",
    "SQL": "Learn databases, queries, joins, grouping, and subqueries.",
    "Git": "Learn Git commands, branches, commits, and GitHub workflows.",
    "Machine Learning": "Learn supervised learning, unsupervised learning, and model evaluation.",
    "Data Structures": "Learn arrays, linked lists, stacks, queues, trees, and graphs.",
    "Problem Solving": "Practice algorithms, logical thinking, and coding problems.",
    "Statistics": "Learn probability, distributions, averages, and statistical analysis.",
    "Data Analysis": "Learn data cleaning, visualization, and analysis using Python."
}

if skills:
    required = required_skills[target_role]

    missing_skills = [
        skill for skill in required
        if skill not in skills
    ]

    if missing_skills:
        st.write("Based on your target role, SkillSync recommends learning:")

        for recommended_skill in missing_skills:
            st.info(
                f"📚 **{recommended_skill}** — "
                f"{skill_recommendations.get(recommended_skill, 'Start learning the fundamentals of this skill.')}"
            )
    else:
        st.success(
            "🎉 You already have the required skills for this role!"
        )

else:
    st.info("Select your skills first to receive recommendations.")
# Skill Progress Tracker
st.divider()

st.header("📈 Skill Progress Tracker")

if skills:
    required = required_skills[target_role]

    skill_status = {}

    for skill in required:
        skill_status[skill] = st.checkbox(
            f"Have you completed {skill}?",
            key=f"progress_{skill}"
        )

    completed_skills = [
        skill for skill, completed in skill_status.items()
        if completed
    ]

    total_skills = len(required)
    completed_count = len(completed_skills)

    progress = completed_count / total_skills

    st.subheader("Your Progress")

    st.progress(progress)

    st.write(
        f"**{completed_count} / {total_skills} skills completed**"
    )

    if progress == 1:
        st.success("🎉 Excellent! You have completed your skill roadmap!")
    elif progress >= 0.5:
        st.success("🔥 You're more than halfway there!")
    else:
        st.info("💪 Keep learning and building your skills!")

else:
    st.info(
        "Select your skills and target career to track your progress."
    )
# Career Readiness Score
st.divider()

st.header("🎯 Career Readiness Score")

if skills:
    required = required_skills[target_role]

    matched_skills = [
        skill for skill in required
        if skill in skills
    ]

    total_required = len(required)
    total_matched = len(matched_skills)

    readiness_score = (total_matched / total_required) * 100

    st.metric(
        "Career Readiness",
        f"{readiness_score:.0f}%"
    )

    st.progress(readiness_score / 100)

    if readiness_score >= 80:
        st.success(
            "🌟 Excellent! You are well prepared for this career."
        )
    elif readiness_score >= 50:
        st.warning(
            "👍 Good progress! Focus on your remaining skill gaps."
        )
    else:
        st.info(
            "💪 You have a good starting point. Keep developing your skills."
        )

else:
    st.info(
        "Select your skills and target career to calculate your readiness score."
    )
matched_skills = [
    skill for skill in required
    if skill in skills
]

readiness_score = (
    len(matched_skills) / len(required)
) * 100
# Career Profile Summary
st.divider()

st.header("📄 Career Profile Summary")

# Check profile details
if name.strip() and course.strip() and len(skills) > 0:

    st.subheader("👤 Personal Information")

    st.write(f"**Name:** {name}")
    st.write(f"**Course:** {course}")
    st.write(f"**Year:** {year}")
    st.write(f"**Target Career:** {target_role}")

    st.subheader("💻 Current Skills")

    for user_skill in skills:
        st.write(f"✅ {user_skill}")

    # Required skills
    required = required_skills[target_role]

    # Find missing skills
    missing_skills = [
        skill for skill in required
        if skill not in skills
    ]

    st.subheader("📌 Skills to Improve")

    if missing_skills:
        for missing_skill in missing_skills:
            st.write(f"🔴 {missing_skill}")
    else:
        st.success("🎉 No skill gaps found!")

    # Readiness score
    matched_skills = [
        skill for skill in required
        if skill in skills
    ]

    readiness_score = (
        len(matched_skills) / len(required)
    ) * 100

    st.subheader("🎯 Career Readiness")

    st.metric(
        "Readiness Score",
        f"{readiness_score:.0f}%"
    )

else:
    st.warning(
        "Please enter your name, course, and select at least one skill."
    )