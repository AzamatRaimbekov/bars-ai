export type Lang = "ru" | "en";

const translations = {
  // ===== COMMON =====
  "app.name.path": { en: "Bars", ru: "Bars" },
  "app.name.mind": { en: "AI", ru: "AI" },
  "app.tagline": { en: "AI-Powered Learning", ru: "Обучение с ИИ" },
  "app.version": { en: "Bars AI v1.0", ru: "Bars AI v1.0" },
  "common.back": { en: "Back", ru: "Назад" },
  "common.continue": { en: "Continue", ru: "Продолжить" },
  "common.start": { en: "Start", ru: "Начать" },
  "common.submit": { en: "Submit", ru: "Отправить" },
  "common.close": { en: "Close", ru: "Закрыть" },
  "common.loading": { en: "Loading...", ru: "Загрузка..." },
  "common.days": { en: "days", ru: "дн." },
  "common.day": { en: "day", ru: "день" },
  "common.min": { en: "min", ru: "мин" },
  "common.lessons": { en: "lessons", ru: "уроков" },
  "common.of": { en: "of", ru: "из" },
  "common.outOf10": { en: "out of 10", ru: "из 10" },

  // ===== NAVIGATION =====
  "nav.dashboard": { en: "Dashboard", ru: "Главная" },
  "nav.roadmap": { en: "Roadmap", ru: "Дорожная карта" },
  "nav.mentor": { en: "Barsbek", ru: "Barsbek" },
  "nav.simulator": { en: "Simulator", ru: "Тренажёр" },
  "nav.achievements": { en: "Achievements", ru: "Достижения" },
  "nav.leaderboard": { en: "Leaderboard", ru: "Рейтинг" },
  "nav.leagues": { en: "Leagues", ru: "Лиги" },
  "nav.profile": { en: "Profile", ru: "Профиль" },

  // ===== LEAGUES =====
  "leagues.title": { en: "Your League", ru: "Ваша лига" },
  "leagues.xpThisWeek": { en: "XP this week", ru: "XP за неделю" },
  "leagues.nextLeague": { en: "Next league", ru: "Следующая лига" },
  "leagues.xpToNext": { en: "XP to next league", ru: "XP до следующей лиги" },
  "leagues.rank": { en: "Your rank", ru: "Ваше место" },
  "leagues.members": { en: "League Members", ru: "Участники лиги" },
  "leagues.promoted": { en: "Promoted!", ru: "Повышение!" },
  "leagues.relegated": { en: "Relegated", ru: "Понижение" },
  "leagues.bronze": { en: "Bronze", ru: "Бронза" },
  "leagues.silver": { en: "Silver", ru: "Серебро" },
  "leagues.gold": { en: "Gold", ru: "Золото" },
  "leagues.platinum": { en: "Platinum", ru: "Платина" },
  "leagues.diamond": { en: "Diamond", ru: "Алмаз" },

  // ===== TOPBAR =====
  "topbar.morning": { en: "Good morning", ru: "Доброе утро" },
  "topbar.afternoon": { en: "Good afternoon", ru: "Добрый день" },
  "topbar.evening": { en: "Good evening", ru: "Добрый вечер" },

  // ===== ONBOARDING =====
  "onboarding.welcome": { en: "Welcome to", ru: "Добро пожаловать в" },
  "onboarding.choosePath": { en: "Choose your learning path", ru: "Выберите направление обучения" },
  "onboarding.nameLabel": { en: "What's your name?", ru: "Как вас зовут?" },
  "onboarding.namePlaceholder": { en: "Enter your name", ru: "Введите имя" },
  "onboarding.assessment": { en: "Level Assessment", ru: "Оценка уровня" },
  "onboarding.question": { en: "Question", ru: "Вопрос" },
  "onboarding.answerPlaceholder": { en: "Type your answer...", ru: "Введите ваш ответ..." },
  "onboarding.ready": { en: "Your Learning Plan is Ready!", ru: "Ваш план обучения готов!" },
  "onboarding.result": { en: "Assessment Result", ru: "Результат оценки" },
  "onboarding.level.beginner": { en: "Beginner Level", ru: "Начальный уровень" },
  "onboarding.level.intermediate": { en: "Intermediate Level", ru: "Средний уровень" },
  "onboarding.level.advanced": { en: "Advanced Level", ru: "Продвинутый уровень" },
  "onboarding.direction": { en: "Direction", ru: "Направление" },
  "onboarding.planDescription": {
    en: "Your personalized roadmap has been generated with topics tailored to your level.",
    ru: "Персональная дорожная карта создана с учётом вашего уровня.",
  },
  "onboarding.startLearning": { en: "Start Learning", ru: "Начать обучение" },
  "onboarding.chatHi": {
    en: "Hi {name}! I'm going to ask you a few questions to understand your current level. Let's start!",
    ru: "Привет, {name}! Я задам вам несколько вопросов, чтобы понять ваш текущий уровень. Начнём!",
  },
  "onboarding.analyzing": { en: "Great! Let me analyze your answers...", ru: "Отлично! Анализирую ваши ответы..." },

  // ===== DIRECTIONS =====
  "direction.frontend.name": { en: "Frontend Development", ru: "Frontend-разработка" },
  "direction.frontend.desc": {
    en: "Master HTML, CSS, JavaScript, React and modern web development",
    ru: "Освойте HTML, CSS, JavaScript, React и современную веб-разработку",
  },
  "direction.english.name": { en: "English Language", ru: "Английский язык" },
  "direction.english.desc": {
    en: "Improve your business and conversational English skills",
    ru: "Улучшите навыки делового и разговорного английского",
  },
  "direction.callcenter.name": { en: "Call Center Training", ru: "Обучение Call Center" },
  "direction.callcenter.desc": {
    en: "Learn customer service, conflict resolution, and communication",
    ru: "Научитесь работе с клиентами, решению конфликтов и коммуникации",
  },
  "direction.cib.name": { en: "CIB Banking", ru: "Корпоративный банкинг" },
  "direction.cib.desc": {
    en: "Corporate & Investment Banking concepts, operations, and interview prep",
    ru: "Концепции корпоративного и инвестиционного банкинга, операции и подготовка к интервью",
  },

  // ===== DASHBOARD =====
  "dashboard.continueLearning": { en: "Continue Learning", ru: "Продолжить обучение" },
  "dashboard.topicsCompleted": { en: "topics completed", ru: "тем пройдено" },
  "dashboard.stats.lessons": { en: "Lessons", ru: "Уроки" },
  "dashboard.stats.hours": { en: "Hours", ru: "Часы" },
  "dashboard.stats.streak": { en: "Streak", ru: "Серия" },
  "dashboard.stats.badges": { en: "Badges", ru: "Награды" },
  "dashboard.aiTip": { en: "AI Tip of the Day", ru: "Совет ИИ на сегодня" },
  "dashboard.tipLoading": {
    en: "Loading your personalized tip...",
    ru: "Загружаем персональный совет...",
  },
  "dashboard.tipFallback": {
    en: "Keep learning every day — consistency beats intensity!",
    ru: "Учитесь каждый день — постоянство важнее интенсивности!",
  },
  "dashboard.chatWith": { en: "Chat with {name}", ru: "Чат с {name}" },
  "dashboard.aiMentor": { en: "Barsbek", ru: "Barsbek" },
  "dashboard.practiceInterview": { en: "Practice Interview", ru: "Тренировка интервью" },
  "dashboard.simulator": { en: "Simulator", ru: "Тренажёр" },
  "dashboard.viewAchievements": { en: "View Achievements", ru: "Достижения" },
  "dashboard.badgesEarned": { en: "badges earned", ru: "наград получено" },

  // ===== ROADMAP =====
  "roadmap.startWithAI": { en: "Start with Barsbek", ru: "Начать с Barsbek" },
  "roadmap.completePrevious": { en: "Complete previous lessons to unlock", ru: "Пройдите предыдущие уроки, чтобы разблокировать" },

  // ===== MENTOR =====
  "mentor.aiMentor": { en: "Barsbek", ru: "Barsbek" },
  "mentor.askAnything": { en: "Ask Barsbek anything...", ru: "Спросите Barsbek что угодно..." },
  "mentor.greeting": {
    en: "Hi! I'm Barsbek, your AI learning assistant from Bars AI. Ask me anything or switch to Voice Mode for a conversation.",
    ru: "Салам! Я Barsbek — ваш ИИ-ассистент на платформе Bars AI. Спрашивайте что угодно или включите голосовой режим для разговора.",
  },
  "mentor.voiceModeOn": { en: "Voice Mode ON", ru: "Голос ВКЛ" },
  "mentor.voiceModeOff": { en: "Voice Mode OFF", ru: "Голос ВЫКЛ" },
  "mentor.voiceModeActive": { en: "Voice Mode active — speak to chat", ru: "Голосовой режим — говорите" },
  "mentor.textMode": { en: "Text Mode", ru: "Текстовый режим" },
  "mentor.error": { en: "Sorry, I encountered an error. Please try again.", ru: "Извините, произошла ошибка. Попробуйте снова." },

  // ===== VOICE =====
  "voice.idle": { en: "Tap the mic to start talking", ru: "Нажмите на микрофон, чтобы начать" },
  "voice.listening": { en: "Listening...", ru: "Слушаю..." },
  "voice.thinking": { en: "Thinking...", ru: "Думаю..." },
  "voice.speaking": { en: "Speaking...", ru: "Говорю..." },
  "voice.tapToStop": { en: "Tap to stop", ru: "Нажмите, чтобы остановить" },
  "voice.tapToInterrupt": { en: "Tap to interrupt", ru: "Нажмите, чтобы прервать" },
  "voice.tapToSpeak": { en: "Tap to speak", ru: "Нажмите, чтобы говорить" },

  // ===== SIMULATOR =====
  "sim.title": { en: "Interview Simulator", ru: "Тренажёр интервью" },
  "sim.chooseMode": { en: "Choose a mode to practice", ru: "Выберите режим тренировки" },
  "sim.technical": { en: "Technical Interview", ru: "Техническое интервью" },
  "sim.technicalDesc": { en: "Answer technical questions with AI evaluation", ru: "Отвечайте на технические вопросы с оценкой ИИ" },
  "sim.situation": { en: "Situation Simulator", ru: "Ситуационный тренажёр" },
  "sim.situational": { en: "Situational", ru: "Ситуационное" },
  "sim.situationDesc": { en: "Practice real-world customer scenarios", ru: "Практикуйте реальные сценарии с клиентами" },
  "sim.voice": { en: "Voice Interview", ru: "Голосовое интервью" },
  "sim.voiceDesc": { en: "Fully voice-based interview simulation", ru: "Полностью голосовая симуляция интервью" },
  "sim.interviewer": { en: "Interviewer", ru: "Интервьюер" },
  "sim.interview": { en: "Interview", ru: "Интервью" },
  "sim.readyToBegin": { en: "Ready to begin your interview?", ru: "Готовы начать интервью?" },
  "sim.startInterview": { en: "Start Interview", ru: "Начать интервью" },
  "sim.typeAnswer": { en: "Type your answer...", ru: "Введите ваш ответ..." },
  "sim.evaluating": { en: "Evaluating...", ru: "Оценка..." },
  "sim.submitAnswer": { en: "Submit Answer", ru: "Отправить ответ" },
  "sim.nextQuestion": { en: "Next Question", ru: "Следующий вопрос" },
  "sim.finishInterview": { en: "Finish Interview", ru: "Завершить интервью" },
  "sim.complete": { en: "Interview Complete!", ru: "Интервью завершено!" },
  "sim.avgScore": { en: "Average Score", ru: "Средний балл" },
  "sim.backToMenu": { en: "Back to Menu", ru: "Вернуться в меню" },
  "sim.transcript": { en: "Transcript", ru: "Стенограмма" },
  "sim.score": { en: "Score", ru: "Балл" },
  "sim.feedback": { en: "Feedback", ru: "Обратная связь" },
  "sim.modelAnswer": { en: "Model Answer", ru: "Образцовый ответ" },
  "sim.question": { en: "Question", ru: "Вопрос" },
  "sim.xpEarned": { en: "XP earned!", ru: "XP получено!" },
  "sim.questionProgress": { en: "Question {current}/{total}", ru: "Вопрос {current}/{total}" },
  "sim.scoreLabel": { en: "Score", ru: "Оценка" },
  "sim.couldNotEvaluate": { en: "Could not evaluate. Try again.", ru: "Не удалось оценить. Попробуйте снова." },

  // ===== LESSON =====
  "lesson.comingSoon": { en: "Lesson content coming soon!", ru: "Содержание урока скоро появится!" },
  "lesson.goBack": { en: "Go Back", ru: "Вернуться" },
  "lesson.perfect": { en: "Perfect!", ru: "Идеально!" },
  "lesson.greatJob": { en: "Great Job!", ru: "Отличная работа!" },
  "lesson.complete": { en: "Lesson Complete!", ru: "Урок пройден!" },
  "lesson.noMistakes": { en: "No mistakes — flawless!", ru: "Без ошибок — безупречно!" },
  "lesson.mistakes": { en: "{count} mistake(s)", ru: "Ошибок: {count}" },
  "lesson.retry": { en: "Retry", ru: "Заново" },
  "lesson.backToMap": { en: "Back to Map", ru: "К карте" },
  "lesson.quiz": { en: "Quiz", ru: "Тест" },
  "lesson.submitQuiz": { en: "Submit Quiz", ru: "Отправить ответы" },
  "lesson.perfectScore": { en: "Perfect score!", ru: "Отличный результат!" },
  "lesson.goodEffort": { en: "Good effort! Review the correct answers above.", ru: "Хорошая работа! Посмотрите правильные ответы выше." },
  "lesson.xpEarned": { en: "XP earned!", ru: "XP получено!" },

  // ===== ACHIEVEMENTS =====
  "achievements.title": { en: "Achievements", ru: "Достижения" },
  "achievements.unlocked": { en: "badges unlocked", ru: "наград открыто" },
  "achievements.streak": { en: "Learning Streak", ru: "Серия обучения" },
  "achievements.badgeUnlocked": { en: "Badge Unlocked!", ru: "Награда получена!" },

  // ===== PROFILE =====
  "profile.assessmentLevel": { en: "Assessment Level", ru: "Уровень оценки" },
  "profile.currentStreak": { en: "Current Streak", ru: "Текущая серия" },
  "profile.lessonsCompleted": { en: "Lessons Completed", ru: "Уроков пройдено" },
  "profile.topicsCompleted": { en: "Topics Completed", ru: "Тем пройдено" },
  "profile.badgesEarned": { en: "Badges Earned", ru: "Наград получено" },
  "profile.nextLevel": { en: "Next Level", ru: "Следующий уровень" },
  "profile.maxLevel": { en: "Max Level!", ru: "Макс. уровень!" },
  "profile.reset": { en: "Reset All Progress", ru: "Сбросить весь прогресс" },
  "profile.resetConfirm": {
    en: "This will reset all your progress. Are you sure?",
    ru: "Это сбросит весь ваш прогресс. Вы уверены?",
  },
  "profile.language": { en: "Language", ru: "Язык" },

  // ===== GAMIFICATION =====
  "gamification.levelUp": { en: "Level Up!", ru: "Новый уровень!" },
  "gamification.keepGoing": {
    en: "Keep going — you're making amazing progress!",
    ru: "Продолжайте — вы делаете отличные успехи!",
  },

  // ===== LEVELS =====
  "level.Novice": { en: "Novice", ru: "Новичок" },
  "level.Apprentice": { en: "Apprentice", ru: "Ученик" },
  "level.Practitioner": { en: "Practitioner", ru: "Практикант" },
  "level.Expert": { en: "Expert", ru: "Эксперт" },
  "level.Master": { en: "Master", ru: "Мастер" },
  "level.Legend": { en: "Legend", ru: "Легенда" },

  // ===== BADGES =====
  "badge.firstStep": { en: "First Step", ru: "Первый шаг" },
  "badge.firstStepDesc": { en: "Complete your first lesson", ru: "Пройдите первый урок" },
  "badge.fastLearner": { en: "Fast Learner", ru: "Быстрый ученик" },
  "badge.fastLearnerDesc": { en: "Complete 10 lessons", ru: "Пройдите 10 уроков" },
  "badge.voiceWarrior": { en: "Voice Warrior", ru: "Голосовой воин" },
  "badge.voiceWarriorDesc": { en: "Complete 10 voice sessions", ru: "Пройдите 10 голосовых сессий" },
  "badge.interviewReady": { en: "Interview Ready", ru: "Готов к интервью" },
  "badge.interviewReadyDesc": { en: "Pass 5 interview simulations", ru: "Пройдите 5 симуляций интервью" },
  "badge.weekWarrior": { en: "Week Warrior", ru: "Воин недели" },
  "badge.weekWarriorDesc": { en: "7-day learning streak", ru: "7-дневная серия обучения" },
  "badge.streakLegend": { en: "Streak Legend", ru: "Легенда серий" },
  "badge.streakLegendDesc": { en: "30-day learning streak", ru: "30-дневная серия обучения" },
  "badge.unstoppable": { en: "Unstoppable", ru: "Неостановимый" },
  "badge.unstoppableDesc": { en: "100-day learning streak", ru: "100-дневная серия обучения" },
  "badge.halfWay": { en: "Half Way There", ru: "Полпути пройдено" },
  "badge.halfWayDesc": { en: "Complete 50% of your roadmap", ru: "Пройдите 50% дорожной карты" },
  "badge.roadMaster": { en: "Road Master", ru: "Мастер пути" },
  "badge.roadMasterDesc": { en: "Complete your entire roadmap", ru: "Пройдите всю дорожную карту" },
  "badge.codeWhisperer": { en: "Code Whisperer", ru: "Шёпот кода" },
  "badge.codeWhispererDesc": { en: "Master all Frontend sections", ru: "Освойте все разделы Frontend" },
  "badge.fluentSpeaker": { en: "Fluent Speaker", ru: "Свободная речь" },
  "badge.fluentSpeakerDesc": { en: "Master all English sections", ru: "Освойте все разделы английского" },
  "badge.serviceStar": { en: "Service Star", ru: "Звезда сервиса" },
  "badge.serviceStarDesc": { en: "Master all Call Center sections", ru: "Освойте все разделы Call Center" },
  "badge.financeGuru": { en: "Finance Guru", ru: "Гуру финансов" },
  "badge.financeGuruDesc": { en: "Master all CIB sections", ru: "Освойте все разделы банкинга" },

  // ===== AUTH =====
  "auth.signIn": { en: "Sign In", ru: "Войти" },
  "auth.signUp": { en: "Sign Up", ru: "Регистрация" },
  "auth.createAccount": { en: "Create Account", ru: "Создать аккаунт" },
  "auth.signInSubtitle": { en: "Sign in to continue learning", ru: "Войдите, чтобы продолжить обучение" },
  "auth.signUpSubtitle": { en: "Create your account", ru: "Создайте ваш аккаунт" },
  "auth.noAccount": { en: "Don't have an account?", ru: "Нет аккаунта?" },
  "auth.hasAccount": { en: "Already have an account?", ru: "Уже есть аккаунт?" },
  "auth.email": { en: "Email", ru: "Эл. почта" },
  "auth.password": { en: "Password", ru: "Пароль" },
  "auth.name": { en: "Name", ru: "Имя" },
  "auth.namePlaceholder": { en: "Your name", ru: "Ваше имя" },
  "auth.emailPlaceholder": { en: "your@email.com", ru: "ваш@email.com" },
  "auth.passwordPlaceholder": { en: "At least 8 characters", ru: "Минимум 8 символов" },
  "auth.loginFailed": { en: "Login failed", ru: "Ошибка входа" },
  "auth.registerFailed": { en: "Registration failed", ru: "Ошибка регистрации" },

  // ===== LESSON PLAYER =====
  "lesson.exitTitle": { en: "Exit lesson?", ru: "Выйти из урока?" },
  "lesson.exitMessage": { en: "Your progress will be lost.", ru: "Ваш прогресс будет потерян." },
  "lesson.stay": { en: "Stay", ru: "Остаться" },
  "lesson.exit": { en: "Exit", ru: "Выйти" },

  // ===== PROFILE EXTRA =====
  "profile.courseProgress": { en: "Course Progress", ru: "Прогресс курса" },
  "profile.levelJourney": { en: "Level Journey", ru: "Путь развития" },
  "profile.hours": { en: "Hours", ru: "Часы" },
  "profile.xpToNext": { en: "XP to", ru: "XP до" },
  "profile.logout": { en: "Log Out", ru: "Выйти из аккаунта" },

  // ===== LEADERBOARD =====
  "leaderboard.title": { en: "Leaderboard", ru: "Рейтинг" },
  "leaderboard.weekly": { en: "This Week", ru: "Неделя" },
  "leaderboard.monthly": { en: "This Month", ru: "Месяц" },
  "leaderboard.allTime": { en: "All Time", ru: "Всё время" },
  "leaderboard.you": { en: "You", ru: "Вы" },
  "leaderboard.rank": { en: "Rank", ru: "Место" },
  "leaderboard.empty": { en: "No data yet", ru: "Пока нет данных" },

  // ===== COURSES =====
  "nav.courses": { en: "Courses", ru: "Курсы" },
  "courses.title": { en: "Course Marketplace", ru: "Маркетплейс курсов" },
  "courses.search": { en: "Search courses...", ru: "Поиск курсов..." },
  "courses.all": { en: "All", ru: "Все" },
  "courses.free": { en: "Free", ru: "Бесплатные" },
  "courses.paid": { en: "Paid", ru: "Платные" },
  "courses.popular": { en: "Popular", ru: "Популярные" },
  "courses.newest": { en: "Newest", ru: "Новые" },
  "courses.highestRated": { en: "Highest Rated", ru: "Лучшие" },
  "courses.priceLow": { en: "Price: Low to High", ru: "Цена: по возрастанию" },
  "courses.enrolled": { en: "students", ru: "студентов" },
  "courses.enroll": { en: "Enroll Free", ru: "Записаться бесплатно" },
  "courses.buy": { en: "Buy for", ru: "Купить за" },
  "courses.continue": { en: "Continue Learning", ru: "Продолжить обучение" },
  "courses.curriculum": { en: "Curriculum", ru: "Программа" },
  "courses.reviews": { en: "Reviews", ru: "Отзывы" },
  "courses.writeReview": { en: "Write a Review", ru: "Написать отзыв" },
  "courses.noReviews": { en: "No reviews yet", ru: "Пока нет отзывов" },
  "courses.description": { en: "Description", ru: "Описание" },
  "courses.noCourses": { en: "No courses found", ru: "Курсы не найдены" },
  "courses.markComplete": { en: "Mark Complete", ru: "Завершить урок" },
  "courses.completed": { en: "Completed", ru: "Завершён" },
  "courses.progress": { en: "Progress", ru: "Прогресс" },
  "teach.title": { en: "My Courses", ru: "Мои курсы" },
  "teach.create": { en: "Create Course", ru: "Создать курс" },
  "teach.noCourses": { en: "You haven't created any courses yet", ru: "Вы ещё не создали ни одного курса" },
  "teach.edit": { en: "Edit Course", ru: "Редактировать курс" },
  "teach.info": { en: "Info", ru: "Инфо" },
  "teach.curriculum": { en: "Curriculum", ru: "Программа" },
  "teach.settings": { en: "Settings", ru: "Настройки" },
  "teach.addSection": { en: "Add Section", ru: "Добавить раздел" },
  "teach.addLesson": { en: "Add Lesson", ru: "Добавить урок" },
  "teach.save": { en: "Save", ru: "Сохранить" },
  "teach.publish": { en: "Publish", ru: "Опубликовать" },
  "teach.unpublish": { en: "Unpublish", ru: "Снять с публикации" },
  "teach.draft": { en: "Draft", ru: "Черновик" },
  "teach.published": { en: "Published", ru: "Опубликован" },
  "teach.price": { en: "Price (cents, 0 = free)", ru: "Цена (центы, 0 = бесплатно)" },
  "teach.lessonContent": { en: "Lesson Content (Markdown)", ru: "Содержание урока (Markdown)" },
  "teach.xpReward": { en: "XP Reward", ru: "Награда XP" },

  // ===== ASSESSMENT QUESTIONS =====
  "assessment.frontend.q1": { en: "What experience do you have with HTML and CSS?", ru: "Какой у вас опыт работы с HTML и CSS?" },
  "assessment.frontend.q2": { en: "Have you worked with JavaScript before? If so, what have you built?", ru: "Работали ли вы с JavaScript раньше? Если да, что вы создавали?" },
  "assessment.frontend.q3": { en: "Do you know what React is? Have you used any frameworks?", ru: "Знаете ли вы, что такое React? Использовали ли вы какие-либо фреймворки?" },
  "assessment.frontend.q4": { en: "Can you explain what responsive design means?", ru: "Можете ли вы объяснить, что такое адаптивный дизайн?" },
  "assessment.frontend.q5": { en: "What tools or code editors do you use for development?", ru: "Какие инструменты или редакторы кода вы используете для разработки?" },

  "assessment.english.q1": { en: "How would you describe your current English level?", ru: "Как бы вы описали свой текущий уровень английского?" },
  "assessment.english.q2": { en: "Do you use English at work or in daily life?", ru: "Используете ли вы английский на работе или в повседневной жизни?" },
  "assessment.english.q3": { en: "Can you tell me about your favorite hobby in English?", ru: "Можете ли вы рассказать о своём хобби на английском?" },
  "assessment.english.q4": { en: "What is the most difficult part of English for you?", ru: "Что для вас самое сложное в английском языке?" },
  "assessment.english.q5": { en: "What is your goal with learning English?", ru: "Какова ваша цель в изучении английского?" },

  "assessment.callcenter.q1": { en: "Have you ever worked in customer service or a call center?", ru: "Работали ли вы когда-нибудь в службе поддержки или колл-центре?" },
  "assessment.callcenter.q2": { en: "How would you handle an angry customer?", ru: "Как бы вы поступили с рассерженным клиентом?" },
  "assessment.callcenter.q3": { en: "What do you think makes good customer service?", ru: "Что, по-вашему, делает обслуживание клиентов хорошим?" },
  "assessment.callcenter.q4": { en: "Are you comfortable speaking on the phone for long periods?", ru: "Комфортно ли вам долго разговаривать по телефону?" },
  "assessment.callcenter.q5": { en: "Describe a time you resolved a conflict or problem for someone.", ru: "Опишите случай, когда вы разрешили конфликт или решили чью-то проблему." },

  "assessment.cib.q1": { en: "What do you know about Corporate & Investment Banking?", ru: "Что вы знаете о корпоративном и инвестиционном банкинге?" },
  "assessment.cib.q2": { en: "Have you studied finance or economics?", ru: "Изучали ли вы финансы или экономику?" },
  "assessment.cib.q3": { en: "Can you explain what a bond is?", ru: "Можете ли вы объяснить, что такое облигация?" },
  "assessment.cib.q4": { en: "What financial tools or software have you used (e.g., Excel)?", ru: "Какие финансовые инструменты или программы вы использовали (например, Excel)?" },
  "assessment.cib.q5": { en: "Why are you interested in a career in banking?", ru: "Почему вас интересует карьера в банковской сфере?" },

  // ===== QUESTS =====
  "quests.daily": { en: "Daily Quests", ru: "Ежедневные задания" },
  "quests.reward": { en: "Reward", ru: "Награда" },
  "quests.completed": { en: "Completed!", ru: "Выполнено!" },
  "quests.progress": { en: "{current}/{target}", ru: "{current}/{target}" },
} as const;

export type TranslationKey = keyof typeof translations;

let currentLang: Lang = (localStorage.getItem("pathmind-lang") as Lang) || "ru";

export function setLanguage(lang: Lang) {
  currentLang = lang;
  localStorage.setItem("pathmind-lang", lang);
  window.dispatchEvent(new Event("lang-change"));
}

export function getLanguage(): Lang {
  return currentLang;
}

export function t(key: TranslationKey, params?: Record<string, string>): string {
  const entry = translations[key];
  if (!entry) return key;
  let text: string = entry[currentLang] || entry.en;
  if (params) {
    for (const [k, v] of Object.entries(params)) {
      text = text.replace(`{${k}}`, v);
    }
  }
  return text;
}
