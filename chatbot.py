# --- Step 1: Import required modules ---
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# --- Step 2: Replace with your actual Bot Token from BotFather ---
BOT_TOKEN = "7837024077:AAEVuMAPrg1Bu5dWlu-raiJ_H7gVoZTsIIs"

# --- Step 3: Define your question-answer dictionary ---
qa_dict = {
    "What degrees are offered at Kepler?": """Kepler, a Non-Governmental Organization (NGO), started operating in Rwanda in 2013 under Generation Rwanda’s attributions. Now, it is legally registered in Rwanda, and Kepler College is the higher learning institution registered and accredited in Rwanda which is operating under Kepler.

Kepler College has various programs:
(1) "Kepler College - SNHU program" offers an elite credential through a partnership with Southern New Hampshire University’s innovative College for America program.
(2) HEC-accredited degrees: Currently, Kepler College offers two accredited degrees: the Bachelor of Arts in Project Management and the Bachelor of Science in Business Analytics.""",

    "What are the requirements for admission?": """The admission requirements vary depending on the program you are interested in.

For Kepler College – Southern New Hampshire University (SNHU) degrees, please refer to the Kepler website.

For HEC-accredited degrees (Bachelor of Arts in Project Management and Bachelor of Science in Business Analytics), refer to the Kepler College website under the “Apply” tab.""",

    "Where can I find the application link?": """The application link is always on our website whenever it is open. You get notified if you have subscribed.
For Kepler College-Southern New Hampshire University (SNHU) degrees, refer to the Kepler website. For HEC-accredited degrees (Bachelor of Arts in Project Management and Bachelor of Science in Business Analytics), refer to the Kepler College website/apply tab.""",

    "Is it possible to get more information about the application process?": """Yes, it is possible to get more information about the application. If you are interested, you can do any of the following to learn more about Kepler College degree programs:
1) Visit Kepler and/or Kepler College websites
2) Contact the admission team at admissions@keplercollege.ac.rw and/or +250789773042
3) Contact the Kepler College reception desk at info@kepler.org, info@keplercollege.ac.rw, +250782637318
4) Visit Kepler College Campus located in Gasabo District, Kinyinya Sector at KG 29 Ave 16.""",

    "Are foreigners allowed to apply for admission?": """Kepler College is committed to providing equal opportunities for all applicants, regardless of cultural background, race, ethnicity, age, gender, nationality, or other personal characteristics. We welcome international applicants and ensure that all qualified candidates are given an equal chance for admission, based solely on their ability to meet our admission requirements. At Kepler College, diversity and inclusion are core values that enrich our learning environment and foster a vibrant, global community.""",

    "Can I apply before getting my High School certificate?": """No, you cannot apply without either a high school certificate or result slip, as it is among the application and admission requirements in general.""",

    "How many years do students study to get their Bachelor degrees?": """All degree programs offered at Kepler College last for three academic years (3 years).""",

    "How can I get support on my application?": """You can do either of the following to receive support during your application process:
1) Contact the admission team at admissions@keplercollege.ac.rw and/or +250789773042
2) Contact the Kepler College reception desk at info@kepler.org, info@keplercollege.ac.rw, +250782637318
3) Visit Kepler College Campus located in Gasabo District, Kinyinya Sector at KG 29 Ave 16.""",

    "What happens after submitting my application to Kepler College?": """After submitting your application, you will receive a confirmation notice indicating that your application has been sent to the Kepler College Admissions Office for review. During the application review process, you may receive a phone call and/or email requesting additional information to support your application. Otherwise, official communication regarding the next steps will be sent via email, with reminders sent via SMS.""",

    "How do I know that I have been admitted to Kepler College?": """If you meet the admission requirements, you will receive an email from admissions@keplercollege.ac.rw with details about the next steps.""",

    "Where is Kepler College located?": """Kepler College is located in Kigali city, Gasabo district and Kinyinya sector (KG 29 Ave 16).""",

    "Can I visit Kepler College campus for more information regarding the application process?": """Yes, you can visit us at the campus and get more information regarding the application process. Kepler College is located in Kigali city, Gasabo district and Kinyinya sector (KG 29 Ave 16).""",

    "How many intakes are there in the academic year?": """Admissions are conducted separately for each of our three programs, with one intake per program each year. Admission timelines may vary, so please check our website for the specific timeline of the program you wish to join.""",

    "How can I apply to Kepler College?": """Applications to Kepler College are submitted online through the official website. Applicants need to create an account, complete the application form, and upload required documents, such as academic transcripts and certificates. Click the 'Apply' button on our website to access the application form.""",

    "What documents are required for the application?": """Applicants need to submit copies of their high school certificates, transcripts, national ID or passport, and A' level report cards or equivalence.""",

    "When is the application deadline?": """The application deadlines vary depending on the intake period. It is important to check the website or contact the admissions office for the most accurate and up-to-date deadlines.""",

    "Does Kepler College offer scholarships?": """Yes, Kepler does offer scholarships but under specific circumstances.""",

    "What is the selection process like?": """The selection process includes an initial screening of submitted documents, followed by an entrance exam or interview to assess the applicant's academic potential and fit for the program.""",

    "How long does the admission process take?": """The admission process typically takes a few weeks after the application deadline, including document review, interviews, and final decision notifications.""",

    "What academic programs are offered?": """Kepler College offers programs in various fields, including Business Administration, Communication, Project Management, and Business Analytics. Full details of the programs are available on the website.""",

    "What are the eligibility criteria for enrolling in the Project Management or Business Analytics Program?": """To enroll in either program, applicants must have completed secondary education and possess a high school diploma with at least two principal passes. Additionally, a strong academic record, proficiency in English, and basic knowledge in mathematics or related subjects are required. Note that for the Business Analytics program, a foundational understanding of statistics or computing may be beneficial.""",

    "Is there an entrance exam or assessment for the registration process?": """Yes, Kepler requires applicants to complete an entrance assessment as part of the admission process. This typically includes evaluating the applicants' English proficiency and critical thinking or cognitive skills. However, the nature of the assessment may vary from year to year.""",

    "How can I apply for the Project Management or Business Analytics programs?": """You can apply online through Kepler College's admissions portal by filling out the application form. Ensure to upload necessary documents such as your academic certificates, a copy of your ID, and high school report as required in the form.""",

    "Is there an application fee?": """Yes, an application fee is required as part of the registration process. Be sure to check the most recent fee structure on the Kepler website.""",

    "Can I apply for both programs simultaneously?": """No, applicants are encouraged to apply for one program at a time.""",

    "Is there an age limit for applying?": """No, there is no age limit. Both younger and mature students are welcome to apply, as long as they meet the academic and language requirements.""",

    "Do I need work experience to apply?": """Work experience is not a mandatory requirement for either program, although it may be beneficial, especially for the Project Management program. Some applicants may have the opportunity to provide professional references.""",

    "Are there options for part-time or distance learning?": """Kepler College does not offer flexible learning schedules in terms of part-time or distance learning. Nevertheless, all content is uploaded on our LMS for the students to access lessons everywhere at any time.""",

    "What language are the courses taught in?": """All courses are taught in English, so a good command of the language is required for success in the program.""",

    "Are there any scholarships or financial aid options available?": """Kepler used to offer scholarships and financial aid options for students who qualify. However, currently, there is no financial aid as per the information highlighted on the website. Prospective students are encouraged to inquire about available opportunities during the admission process.""",

    "Can international students apply for financial aid?": """Yes, international students are eligible to apply for financial aid, but the availability of these funds may differ based on the country of origin, program, and financial need.""",

    "How will I know if I am accepted into the program?": """After completing the application process, including any assessments and interviews, you will receive a formal notification via email if you are accepted. Kepler will provide specific details about the next steps and any requirements for finalizing your admission.""",

    "What happens after I receive my acceptance letter?": """Once you receive your acceptance letter, you will be required to confirm your intention to enroll by a specified deadline. You may also be asked to submit additional documents, complete registration forms, and finalize your financial aid package (if applicable).""",

    "Can I defer my admission after being accepted?": """Yes, students may request to defer their admission for one academic year. However, deferral requests are considered on a case-by-case basis, and approval is not guaranteed.""",

    "What happens if my application is rejected?": """If your application is rejected, you will receive a notification from the admissions team. You may be given feedback on areas for improvement, and you can reapply during the next admission cycle.""",

    "What support services are available for new students?": """Kepler offers a range of support services for new students, including academic advising, career counseling, mentorship programs, and student orientation sessions to help students adjust to college life and their coursework.""",

    "What kind of jobs can I get after completing the Project Management program?": """Graduates of the Project Management program can pursue various roles such as Project Manager, Program Coordinator, Operations Manager, or Project Analyst in industries like construction, IT, healthcare, marketing, and finance.""",

    "What career paths are available for Business Analytics graduates?": """Business Analytics graduates can find career opportunities in data analysis, business intelligence, market research, financial analysis, and consulting. Common job titles include Data Analyst, Business Analyst, Financial Analyst, and Market Research Analyst.""",

    "Will I receive a certification upon completing the program?": """Yes, upon successful completion of the Project Management or Business Analytics programs, you will receive a formal certification that can boost your qualifications in the job market.""",

    "What is the curriculum like for the Project Management Program?": """The Project Management curriculum at Kepler includes foundational courses in project planning, risk management, budgeting, stakeholder communication, and the use of project management tools like Microsoft Project or other software. The program also includes practical experience through case studies and real-world projects.""",

    "Is there an interview as part of the admissions process?": """Yes, after the initial assessment, shortlisted applicants are invited for an interview. This is an important step in the admissions process and helps the admissions team assess the applicant's communication skills, motivation, and suitability for the program.""",

    "What is the medium of instruction at Kepler College?": """The medium of instruction at Kepler is English. All courses, materials, and communications are conducted in English, so fluency in the language is necessary for success.""",

    "Does Kepler accept mature students?": """Yes, Kepler accepts mature students who may have been out of school for a period. All that is needed is to meet the general admission criteria, and their applications will be considered.""",

    "How long does it take to complete a degree at Kepler?": """The duration of the degree programs at Kepler depends on the specific program and the student's pace of study in the SNHU program. For the Business Analytics and Project Management, the duration is 3 years.""",

    "What kinds of extracurricular development opportunities does Kepler offer?": """Kepler provides leadership development programs, entrepreneurship training, community service projects, and networking opportunities. These activities help students develop professional skills and personal growth outside of the classroom.""",

    "How are students assessed during the program?": """Assessment at Kepler includes a mix of exams, coursework, group projects, presentations, and practical assignments. Students are evaluated continuously to ensure they meet academic standards and develop the necessary skills for their chosen field.""",

    "Can students work while studying at Kepler?": """No, students cannot work while studying because we need them to stay on track. This applies mainly to the two programs, Business Analytics and Project Management. However, students in the SNHU program can find job opportunities as long as they stay on track with their academic journey.""",

    "Is there a dress code for students at Kepler?": """While there is no strict uniform requirement, students are expected to dress appropriately and professionally, especially during formal events or interactions with external partners.""",

    "What happens if I fall behind in my studies?": """If a student is struggling academically, Kepler offers academic support services, including tutoring, study groups, and one-on-one mentoring. Early intervention is encouraged to help students stay on track with their coursework."""
}


# --- Step 4: Define a message handler ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.strip()
    response = qa_dict.get(user_message, "Sorry, I couldn’t find an answer to that question. Please try rephrasing.")
    await update.message.reply_text(response)

# --- Step 5: Define a start command handler ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = "👋 Welcome to Kepler College Admissions Bot!\nAsk me any question from the FAQ."
    await update.message.reply_text(welcome_message)

# --- Step 6: Main function to run the bot ---
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print(" Bot is running...")
    app.run_polling()
