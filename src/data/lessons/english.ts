import type { LessonContent } from "../lessons";

export const ENGLISH_LESSONS: Record<string, LessonContent> = {
  "en-1-1": {
    id: "en-1-1",
    title: "Sounds & Phonetics",
    content: `# English Sounds & Phonetics

The English alphabet has 26 letters, but the language contains approximately 44 distinct sounds (phonemes). Understanding these sounds is the foundation for clear pronunciation and effective communication.

## Vowel Sounds

English has short vowels, long vowels, and diphthongs. Short vowels include /ɪ/ as in "sit," /ɛ/ as in "bed," /æ/ as in "cat," /ʌ/ as in "cup," /ɒ/ as in "hot," and /ʊ/ as in "put." Long vowels are held longer: /iː/ as in "see," /ɑː/ as in "car," /ɔː/ as in "door," /uː/ as in "blue," and /ɜː/ as in "bird." Diphthongs are gliding vowels where the sound changes within the same syllable, such as /aɪ/ in "time," /eɪ/ in "day," and /ɔɪ/ in "boy."

## Consonant Sounds

Consonants are produced by partially or fully blocking airflow. Key distinctions include voiced vs. voiceless pairs: /b/ vs. /p/, /d/ vs. /t/, /g/ vs. /k/, /v/ vs. /f/, /z/ vs. /s/. Place your hand on your throat — if you feel vibration, the sound is voiced. English also has unique consonant sounds that many learners struggle with, such as /θ/ (thin) and /ð/ (this), which require placing the tongue between the teeth.

## The International Phonetic Alphabet (IPA)

The IPA is a standardized system for representing sounds. Every English dictionary uses IPA transcriptions to show pronunciation. For example, the word "through" is transcribed as /θruː/. Learning to read IPA will help you pronounce any new word correctly, even before you hear it spoken. Start by memorizing the IPA symbols for the 44 English phonemes, and use online dictionaries that include audio playback alongside IPA transcriptions.

## Practical Tips

Practice minimal pairs — words that differ by only one sound (e.g., "ship" vs. "sheep," "bat" vs. "bet"). Record yourself and compare with native speakers. Focus on sounds that do not exist in your native language, as these will require the most attention.`,
    videos: [
      { title: "All English Sounds with IPA Symbols", url: "https://www.youtube.com/watch?v=dfoRdKuPF9I", duration: "18:20" },
      { title: "English Pronunciation - Vowel Sounds", url: "https://www.youtube.com/watch?v=LMhq4Vqaxnk", duration: "15:45" },
      { title: "44 Phonemes of English", url: "https://www.youtube.com/watch?v=9rzU-0Oqz44", duration: "12:30" },
    ],
    quiz: [
      {
        question: "How many distinct sounds (phonemes) does English approximately have?",
        options: ["26", "36", "44", "52"],
        correct: 2,
      },
      {
        question: "Which pair of sounds are 'voiced' and 'voiceless' counterparts?",
        options: ["/b/ and /d/", "/b/ and /p/", "/m/ and /n/", "/s/ and /z/ and /b/ and /d/"],
        correct: 1,
      },
      {
        question: "What does IPA stand for?",
        options: ["International Pronunciation Association", "International Phonetic Alphabet", "Internal Phonics Application", "International Phone Alphabet"],
        correct: 1,
      },
    ],
    flashCards: [
      { front: "/iː/", back: "Long 'ee' as in 'see'" },
      { front: "/æ/", back: "Short 'a' as in 'cat'" },
      { front: "/θ/", back: "'th' as in 'think' (voiceless)" },
      { front: "/ð/", back: "'th' as in 'this' (voiced)" },
      { front: "/ʃ/", back: "'sh' as in 'ship'" },
      { front: "/ʒ/", back: "'zh' as in 'measure'" },
      { front: "/ŋ/", back: "'ng' as in 'sing'" },
      { front: "/aɪ/", back: "Diphthong as in 'time'" },
    ],
    matchGame: [
      { term: "Vowel", definition: "A, E, I, O, U sounds" },
      { term: "Consonant", definition: "All non-vowel sounds" },
      { term: "Diphthong", definition: "Gliding vowel (two sounds in one)" },
      { term: "Voiced", definition: "Vocal cords vibrate (/b/, /d/, /g/)" },
      { term: "Voiceless", definition: "No vibration (/p/, /t/, /k/)" },
    ],
  },

  "en-2-1": {
    id: "en-2-1",
    title: "SVO Structure",
    content: `# Subject-Verb-Object (SVO) Structure

English is an SVO language, meaning the standard word order in a sentence is Subject + Verb + Object. This is the backbone of almost every English sentence and understanding it is critical for constructing grammatically correct statements.

## The Three Components

**Subject** — the person or thing performing the action. It answers "Who?" or "What?" Examples: "She," "The dog," "My manager."

**Verb** — the action or state. It tells us what the subject does or is. Examples: "reads," "is running," "has completed."

**Object** — the person or thing receiving the action. It answers "What?" or "Whom?" Examples: "a book," "the report," "her friend."

## Examples in Practice

- "She (S) reads (V) books (O)."
- "The team (S) finished (V) the project (O)."
- "I (S) love (V) pizza (O)."

Not every sentence requires an object. Intransitive verbs work without one: "She (S) smiled (V)." "The baby (S) is sleeping (V)."

## Word Order Matters

Unlike many languages that use case endings to show grammatical roles, English relies heavily on word order. Changing the order changes the meaning entirely: "The dog bit the man" vs. "The man bit the dog." The subject always comes first in declarative sentences, which is why SVO order is so important.

## Building Longer Sentences

You can expand SVO sentences by adding adjectives, adverbs, and prepositional phrases without changing the core structure: "The experienced team (S) quickly finished (V) the complex project (O) before the deadline." The SVO skeleton remains the same — everything else is decoration.`,
    videos: [
      { title: "English Sentence Structure - SVO", url: "https://www.youtube.com/watch?v=LGaM_L0MHqY", duration: "10:15" },
      { title: "Basic English Word Order", url: "https://www.youtube.com/watch?v=oM2m1Rqh0eY", duration: "8:42" },
    ],
    quiz: [
      {
        question: "In the sentence 'Maria reads newspapers,' what is the object?",
        options: ["Maria", "reads", "newspapers", "There is no object"],
        correct: 2,
      },
      {
        question: "What does SVO stand for?",
        options: ["Simple Verb Order", "Subject-Verb-Object", "Sentence Vocabulary Order", "Standard Verbal Output"],
        correct: 1,
      },
    ],
  },

  "en-2-2": {
    id: "en-2-2",
    title: "Simple Sentences",
    content: `# Building Simple Sentences

A simple sentence contains one independent clause — a subject and a predicate that express a complete thought. Mastering simple sentences is essential before moving to compound and complex structures.

## Types of Simple Sentences

**Declarative** — makes a statement: "The sun rises in the east." These end with a period and are the most common type in everyday communication.

**Interrogative** — asks a question: "Do you speak English?" These use inverted word order (verb before subject) or question words (who, what, where, when, why, how).

**Imperative** — gives a command or request: "Close the door." The subject "you" is implied and not stated.

**Exclamatory** — expresses strong emotion: "What a beautiful day!" These end with an exclamation mark.

## Articles: A, An, The

Articles are small words that make a big difference. Use "a" before consonant sounds ("a book," "a university") and "an" before vowel sounds ("an apple," "an hour"). Use "the" when referring to something specific that both speaker and listener know about: "The book on the table is mine." Omit articles with uncountable nouns in general statements: "Water is essential for life."

## Forming Negative Sentences

Add "not" after the auxiliary verb: "She does not (doesn't) like coffee." "They are not (aren't) coming." "He has not (hasn't) finished." For sentences without an auxiliary, add "do/does/did + not": "I do not agree." This is one of the most common patterns in everyday English.

## Common Mistakes to Avoid

- Missing articles: "I need book" should be "I need a book."
- Double negatives: "I don't have nothing" should be "I don't have anything."
- Missing subject: "Is raining" should be "It is raining." English requires explicit subjects (unlike some languages).`,
    videos: [
      { title: "How to Make Simple Sentences in English", url: "https://www.youtube.com/watch?v=GZOk7MOsMOo", duration: "11:30" },
      { title: "English Articles - A, An, The", url: "https://www.youtube.com/watch?v=KyOvBQ87aP4", duration: "14:20" },
    ],
    quiz: [
      {
        question: "Which sentence is imperative?",
        options: ["She is reading.", "Is she reading?", "Open the window.", "What a great movie!"],
        correct: 2,
      },
      {
        question: "Which article goes before 'honest person'?",
        options: ["a", "an", "the", "no article"],
        correct: 1,
      },
      {
        question: "How do you make 'She likes tea' negative?",
        options: ["She not likes tea.", "She doesn't like tea.", "She no like tea.", "She likes not tea."],
        correct: 1,
      },
    ],
  },

  "en-3-1": {
    id: "en-3-1",
    title: "Present Simple",
    content: `# Present Simple Tense

The Present Simple is one of the most frequently used tenses in English. It describes habits, routines, general truths, and permanent situations.

## When to Use Present Simple

1. **Habits and routines**: "I wake up at 7 AM every day." "She drinks coffee every morning."
2. **General truths and facts**: "The Earth revolves around the Sun." "Water boils at 100°C."
3. **Permanent situations**: "He works at a bank." "They live in London."
4. **Schedules and timetables**: "The train leaves at 9:15." "The meeting starts at 2 PM."

## How to Form It

For most verbs, use the base form: I/you/we/they + verb ("I work," "They play"). For he/she/it, add -s or -es: "He works," "She watches," "It goes." Spelling rules for third person: add -es after -s, -sh, -ch, -x, -o ("watches," "goes," "fixes"); change -y to -ies after a consonant ("studies," "carries") but keep -y after a vowel ("plays," "enjoys").

## Negative Form

Use do not (don't) / does not (doesn't) + base verb: "I don't like spicy food." "She doesn't work on weekends." Note: the main verb stays in base form after doesn't — "She doesn't works" is WRONG.

## Question Form

Use Do/Does + subject + base verb: "Do you speak French?" "Does he live here?" Short answers: "Yes, I do." / "No, he doesn't." For information questions, add a question word: "Where do you work?" "What does she study?"

## Key Time Expressions

Every day, always, usually, often, sometimes, rarely, never, once a week, on Mondays, in the morning. These adverbs of frequency go before the main verb but after "be": "She always arrives on time." "He is always late."`,
    videos: [
      { title: "Present Simple Tense - English Grammar", url: "https://www.youtube.com/watch?v=cGA-eKSYfLI", duration: "12:45" },
      { title: "Present Simple: All Forms Explained", url: "https://www.youtube.com/watch?v=_3TmOqR5xOo", duration: "16:30" },
    ],
    quiz: [
      {
        question: "Which sentence correctly uses the Present Simple?",
        options: ["She is work every day.", "She works every day.", "She working every day.", "She work every day."],
        correct: 1,
      },
      {
        question: "How do you form the negative of 'He plays tennis'?",
        options: ["He not plays tennis.", "He don't play tennis.", "He doesn't play tennis.", "He doesn't plays tennis."],
        correct: 2,
      },
      {
        question: "Where does the adverb 'always' go in 'She is late'?",
        options: ["Always she is late.", "She always is late.", "She is always late.", "She is late always."],
        correct: 2,
      },
    ],
  },

  "en-3-2": {
    id: "en-3-2",
    title: "Present Continuous",
    content: `# Present Continuous Tense

The Present Continuous (also called Present Progressive) describes actions happening right now, temporary situations, and future arrangements.

## When to Use Present Continuous

1. **Actions happening now**: "I am reading a book." "She is talking on the phone."
2. **Temporary situations**: "He is staying with friends this week." "I am working from home this month."
3. **Future arrangements**: "We are meeting them tomorrow at 5." "She is flying to Paris next Monday."
4. **Changing or developing situations**: "The climate is getting warmer." "Your English is improving."
5. **Annoying habits (with 'always')**: "He is always losing his keys!" "She is always interrupting me!"

## How to Form It

Subject + am/is/are + verb-ing: "I am working." "She is cooking." "They are playing."

Spelling rules for -ing: drop silent -e ("make → making," "write → writing"); double the final consonant after a short stressed vowel ("run → running," "sit → sitting," "begin → beginning"); -ie changes to -y ("die → dying," "lie → lying").

## Negative and Question Forms

**Negative**: Subject + am/is/are + not + verb-ing: "I am not sleeping." "She isn't listening." "They aren't coming."

**Questions**: Am/Is/Are + subject + verb-ing: "Are you coming?" "Is she working?" Short answers: "Yes, I am." / "No, she isn't."

## Stative Verbs — Do NOT Use with Continuous

Some verbs describe states rather than actions and are not normally used in the continuous form: know, believe, want, need, prefer, love, hate, like, understand, remember, belong, seem, mean, own, have (possession). Say "I know the answer" NOT "I am knowing the answer." Say "She wants coffee" NOT "She is wanting coffee."

## Present Simple vs. Present Continuous

- "I work from home." (permanent/general) vs. "I am working from home this week." (temporary)
- "She speaks French." (ability) vs. "She is speaking French right now." (current action)
- "He plays football." (regular habit) vs. "He is playing football at the moment." (happening now)`,
    videos: [
      { title: "Present Continuous - When and How to Use It", url: "https://www.youtube.com/watch?v=amBqilOsRrE", duration: "13:10" },
      { title: "Present Simple vs Present Continuous", url: "https://www.youtube.com/watch?v=Iu5lMOokLuo", duration: "15:00" },
    ],
    quiz: [
      {
        question: "Which verb should NOT be used in the present continuous?",
        options: ["run", "eat", "know", "play"],
        correct: 2,
      },
      {
        question: "What is the correct form: 'She ___ to music right now'?",
        options: ["listens", "is listening", "listening", "listen"],
        correct: 1,
      },
      {
        question: "Which sentence expresses a future arrangement?",
        options: ["I will go tomorrow.", "I go tomorrow.", "I am going tomorrow.", "I have gone tomorrow."],
        correct: 2,
      },
    ],
  },

  "en-4-1": {
    id: "en-4-1",
    title: "Past & Future",
    content: `# Past Simple and Future Tenses

Being able to talk about the past and the future is essential for telling stories, making plans, and having meaningful conversations.

## Past Simple

Use the Past Simple for completed actions at a specific time in the past.

**Regular verbs** add -ed: "I worked yesterday." "She cleaned the house." Spelling: double the final consonant after a short stressed vowel ("stopped," "planned"); change -y to -ied after a consonant ("studied," "carried").

**Irregular verbs** have unique past forms that must be memorized: go → went, see → saw, take → took, have → had, make → made, come → came, know → knew, think → thought, buy → bought, give → gave.

**Negative**: did not (didn't) + base verb: "I didn't go." "She didn't see him."
**Questions**: Did + subject + base verb: "Did you finish?" "Did she call?"

**Time expressions**: yesterday, last week, two days ago, in 2020, when I was young.

## Future with "Will"

Use "will" for predictions, spontaneous decisions, promises, and offers.

- **Predictions**: "It will rain tomorrow." "AI will change everything."
- **Spontaneous decisions**: "I'll have the pasta." (deciding now) "I'll help you with that."
- **Promises**: "I will always love you." "I won't tell anyone."

**Form**: Subject + will + base verb. Negative: will not (won't). Questions: Will + subject + base verb?

## Future with "Going to"

Use "going to" for plans/intentions and predictions based on evidence.

- **Plans**: "I am going to study abroad next year." "We are going to launch the product in March."
- **Evidence-based predictions**: "Look at those clouds — it is going to rain." "She has studied hard — she is going to pass."

## Will vs. Going To

- "I'll buy some milk." (spontaneous — just decided)
- "I'm going to buy some milk." (planned — already on my list)

Both can express predictions, but "going to" implies visible evidence while "will" implies personal opinion or belief.`,
    videos: [
      { title: "Past Simple Tense - Regular and Irregular Verbs", url: "https://www.youtube.com/watch?v=ex5gDkELXU8", duration: "14:50" },
      { title: "WILL vs GOING TO - Future Tenses", url: "https://www.youtube.com/watch?v=BeBi-Vjfits", duration: "11:25" },
    ],
    quiz: [
      {
        question: "What is the past simple of 'go'?",
        options: ["goed", "gone", "went", "going"],
        correct: 2,
      },
      {
        question: "Which sentence uses 'going to' correctly for a plan?",
        options: [
          "I will to visit Paris.",
          "I am going to visit Paris next summer.",
          "I going to visit Paris.",
          "I am go to visit Paris.",
        ],
        correct: 1,
      },
      {
        question: "'Look out! The vase ___ fall!' Which is more appropriate?",
        options: ["will", "is going to", "would", "shall"],
        correct: 1,
      },
    ],
  },

  "en-5-1": {
    id: "en-5-1",
    title: "Daily Life Words",
    content: `# Everyday Vocabulary

Building a strong everyday vocabulary is the fastest way to become functional in English. The most common 2,000 words in English cover approximately 80% of everyday conversation.

## Greetings & Basics

Essential phrases for daily interaction: "Hello / Hi / Hey" (informal to formal). "Good morning / afternoon / evening." "How are you?" → "I'm fine, thanks." / "Not bad." / "Pretty good." "Nice to meet you." "See you later / Bye / Take care." "Excuse me" (to get attention), "Sorry" (to apologize), "Thank you / Thanks a lot."

## Around the House

**Rooms**: kitchen, bedroom, bathroom, living room, hallway, basement, attic.
**Furniture**: table, chair, sofa, bed, desk, shelf, wardrobe, drawer.
**Appliances**: fridge, oven, microwave, washing machine, dishwasher, vacuum cleaner.
**Daily routine verbs**: wake up, get up, brush teeth, take a shower, get dressed, have breakfast, leave home, come back, cook dinner, go to bed.

## Food & Shopping

**At a restaurant**: "Can I see the menu, please?" "I'd like the chicken salad." "Could I have the bill?" Tip: "I'd like" is more polite than "I want."
**At a store**: "How much is this?" "Do you have this in a larger size?" "I'm just looking, thanks." "Can I pay by card?"
**Common foods**: bread, rice, pasta, chicken, beef, fish, eggs, cheese, milk, fruit, vegetables, butter, oil, salt, pepper, sugar.

## Transportation

**Getting around**: "Where is the nearest bus stop / subway station?" "How do I get to...?" "Is it within walking distance?" "I need a taxi / ride."
**Useful words**: ticket, platform, departure, arrival, connection, delay, one-way, round-trip, fare.

## Numbers, Time & Dates

Master these patterns: "What time is it?" → "It's half past three / a quarter to five / ten minutes after six." Days of the week (Monday through Sunday), months (January through December), ordinal numbers for dates ("the first," "the twenty-third"). "What's the date today?" → "It's April 2nd."`,
    videos: [
      { title: "1000 Most Common English Words", url: "https://www.youtube.com/watch?v=GIy-gLKTCSA", duration: "20:15" },
      { title: "Daily Routine Vocabulary", url: "https://www.youtube.com/watch?v=qcYPJncjDXQ", duration: "12:00" },
    ],
    quiz: [
      {
        question: "What is a more polite way to order food at a restaurant?",
        options: ["I want the salad.", "Give me the salad.", "I'd like the salad, please.", "Salad for me."],
        correct: 2,
      },
      {
        question: "What does 'half past three' mean?",
        options: ["2:30", "3:15", "3:30", "3:45"],
        correct: 2,
      },
    ],
  },

  "en-6-1": {
    id: "en-6-1",
    title: "Office Vocabulary",
    content: `# Work & Office Vocabulary

Workplace English has its own vocabulary and conventions. Whether you work in an office, remotely, or in a hybrid setup, knowing these terms will help you communicate professionally.

## Job Titles & Departments

**Common titles**: Manager, Director, Team Lead, Specialist, Analyst, Coordinator, Associate, Intern, CEO, CTO, CFO, HR Manager.
**Departments**: Human Resources (HR), Marketing, Sales, Finance, IT (Information Technology), Operations, Legal, Customer Support, Research & Development (R&D).

## Office Equipment & Spaces

**Equipment**: laptop, monitor, keyboard, mouse, printer, scanner, projector, whiteboard, headset, charger.
**Spaces**: open office, cubicle, conference room, meeting room, break room, reception, lobby, parking lot.
**Supplies**: stapler, paper clips, sticky notes, folder, binder, envelope, notebook.

## Common Workplace Phrases

**Starting the day**: "Good morning, team." "Let's get started." "What's on the agenda today?"
**Asking for help**: "Could you help me with this?" "Do you have a minute?" "I need your input on something."
**Agreeing**: "That sounds good." "I'm on board." "Let's go with that."
**Disagreeing politely**: "I see your point, but..." "I'm not sure about that." "Have we considered...?"
**Delegating**: "Could you take care of this?" "Can you handle the report?" "I'll leave that to you."

## Email & Communication Verbs

**Key verbs**: send, reply, forward, CC (carbon copy), BCC (blind carbon copy), attach, schedule, confirm, follow up, escalate, update, submit, approve, reject, postpone, cancel.

**Phrases**: "As per our conversation..." "Please find attached..." "I wanted to follow up on..." "Just to confirm..." "Let me circle back on that." "I'll keep you posted." "Let's touch base next week."

## Talking About Your Job

"I work at [company name]." "I work in [department/field]." "I'm responsible for [task]." "My main duties include [tasks]." "I report to [person/title]." "I've been with the company for [time]." These phrases help you introduce your professional role clearly.`,
    videos: [
      { title: "Office Vocabulary in English", url: "https://www.youtube.com/watch?v=FWpcQLTJ_dI", duration: "13:40" },
      { title: "Business English - Workplace Phrases", url: "https://www.youtube.com/watch?v=Oj0G9gHoEMY", duration: "16:20" },
    ],
    quiz: [
      {
        question: "What does 'CC' mean in email?",
        options: ["Correct Copy", "Carbon Copy", "Company Communication", "Confirmed Contact"],
        correct: 1,
      },
      {
        question: "Which phrase is a polite way to disagree in a meeting?",
        options: ["You're wrong.", "That's a terrible idea.", "I see your point, but...", "No way."],
        correct: 2,
      },
      {
        question: "How do you politely ask a colleague for help?",
        options: ["Help me now.", "Do you have a minute?", "I need this done.", "You should help me."],
        correct: 1,
      },
    ],
  },

  "en-7-1": {
    id: "en-7-1",
    title: "Idioms & Phrasals",
    content: `# Idioms & Phrasal Verbs

Idioms and phrasal verbs are essential for understanding natural English. Native speakers use them constantly in both casual and professional settings.

## Common Idioms

**Everyday idioms**:
- "Break the ice" — to start a conversation in an awkward situation. "He told a joke to break the ice."
- "Hit the nail on the head" — to be exactly right. "You hit the nail on the head with that analysis."
- "A piece of cake" — something very easy. "The exam was a piece of cake."
- "Once in a blue moon" — very rarely. "I eat fast food once in a blue moon."
- "Under the weather" — feeling sick. "I'm feeling a bit under the weather today."
- "The ball is in your court" — it's your decision/turn to act. "I've made my offer — the ball is in your court."
- "Cost an arm and a leg" — very expensive. "That car cost an arm and a leg."
- "Let the cat out of the bag" — to reveal a secret accidentally. "She let the cat out of the bag about the surprise party."

## Essential Phrasal Verbs

Phrasal verbs combine a verb with a preposition or adverb to create a new meaning:

- **Look up** — to search for information. "I looked up the word in the dictionary."
- **Give up** — to stop trying. "Never give up on your dreams."
- **Put off** — to postpone. "They put off the meeting until next week."
- **Turn down** — to reject. "She turned down the job offer."
- **Come up with** — to think of an idea. "We need to come up with a solution."
- **Figure out** — to solve or understand. "I can't figure out this problem."
- **Bring up** — to mention a topic. "Don't bring up politics at dinner."
- **Run out of** — to have no more of something. "We ran out of milk."
- **Look forward to** — to be excited about something future. "I look forward to meeting you."
- **Get along with** — to have a good relationship. "She gets along with everyone."

## Separable vs. Inseparable Phrasal Verbs

Some phrasal verbs can be separated by an object: "Turn the light off" or "Turn off the light" — both correct. With pronouns, you MUST separate: "Turn it off" (NOT "Turn off it").

Inseparable phrasal verbs cannot be split: "I look after my grandmother" (NOT "I look my grandmother after"). "She ran into an old friend" (NOT "She ran an old friend into").

## Tips for Learning

Do not try to memorize long lists. Instead, learn phrasal verbs in context — through stories, conversations, and real-life situations. Group them by particle (all "up" phrasal verbs, all "out" phrasal verbs) or by topic (work, relationships, daily life).`,
    videos: [
      { title: "25 Most Common Phrasal Verbs", url: "https://www.youtube.com/watch?v=JTMi7RjyvJ0", duration: "18:30" },
      { title: "10 English Idioms You Need to Know", url: "https://www.youtube.com/watch?v=7JtBbQFBdIA", duration: "12:15" },
    ],
    quiz: [
      {
        question: "What does 'break the ice' mean?",
        options: ["To break something frozen", "To start a conversation in an awkward setting", "To cancel an event", "To get angry"],
        correct: 1,
      },
      {
        question: "Which is correct?",
        options: ["Turn off it.", "Turn it off.", "Turn it of.", "Off turn it."],
        correct: 1,
      },
      {
        question: "'She ___ the job offer.' (rejected)",
        options: ["turned down", "turned up", "turned on", "turned over"],
        correct: 0,
      },
    ],
  },

  "en-8-1": {
    id: "en-8-1",
    title: "Word Combinations",
    content: `# Collocations — Natural Word Combinations

Collocations are words that naturally go together in English. Using correct collocations makes your English sound fluent and natural, while incorrect combinations sound awkward even if grammatically correct.

## What Are Collocations?

A collocation is a pair or group of words that are frequently used together. For example, we say "make a decision" (NOT "do a decision"), "heavy rain" (NOT "strong rain"), and "fast food" (NOT "quick food"). These combinations are not based on logical rules — they are conventions that native speakers have agreed upon.

## Common Verb + Noun Collocations

**Make**: make a mistake, make a decision, make progress, make an effort, make a phone call, make money, make an appointment, make a suggestion, make friends, make sense.

**Do**: do homework, do the dishes, do a favor, do business, do research, do your best, do damage, do an exercise, do the laundry.

**Take**: take a break, take a shower, take a photo, take notes, take a seat, take responsibility, take a risk, take an exam, take advice, take place.

**Have**: have a meeting, have a conversation, have lunch, have fun, have an experience, have a problem, have an argument, have a look.

**Pay**: pay attention, pay a compliment, pay a visit, pay respect.

## Adjective + Noun Collocations

"Strong" vs. "heavy" vs. "big" — they do not freely interchange:
- strong coffee (NOT powerful coffee), strong wind, strong opinion
- heavy rain (NOT strong rain), heavy traffic, heavy workload
- big mistake (NOT large mistake), big deal, big difference
- deep sleep (NOT strong sleep), deep breath, deep understanding

## Adverb + Adjective Collocations

- "Highly" recommended / unlikely / competitive / skilled
- "Deeply" concerned / moved / committed / affected
- "Fully" aware / equipped / committed / booked
- "Bitterly" disappointed / cold / divided

## How to Learn Collocations

When you learn a new word, always learn it with its common partners. Do not just learn "make" — learn "make a decision," "make progress," "make a mistake." Use a collocations dictionary (like the Oxford Collocations Dictionary) and pay attention to word combinations when you read or listen to English.`,
    videos: [
      { title: "English Collocations with Make and Do", url: "https://www.youtube.com/watch?v=gJ2w3LDBbas", duration: "14:00" },
      { title: "50 Common English Collocations", url: "https://www.youtube.com/watch?v=CwPYSGIMXDQ", duration: "20:45" },
    ],
    quiz: [
      {
        question: "Which collocation is correct?",
        options: ["do a decision", "make a decision", "take a decision", "have a decision"],
        correct: 1,
      },
      {
        question: "We say 'heavy ___' (not 'strong')",
        options: ["coffee", "opinion", "rain", "wind"],
        correct: 2,
      },
      {
        question: "Which is the correct collocation?",
        options: ["pay attention", "make attention", "do attention", "give attention"],
        correct: 0,
      },
    ],
  },

  "en-9-1": {
    id: "en-9-1",
    title: "Self-Introduction",
    content: `# Introducing Yourself in English

A strong self-introduction sets the tone for any interaction. Whether in a social setting, a job interview, or a business meeting, knowing how to present yourself confidently in English is a key skill.

## The Basic Structure

A good self-introduction covers these elements in order:

1. **Greeting**: "Hello," "Hi," "Good morning/afternoon."
2. **Name**: "My name is..." or "I'm..."
3. **Where you're from**: "I'm from..." or "I come from..."
4. **What you do**: "I work as a..." "I'm a [job title] at [company]." "I'm a student at..."
5. **A personal detail**: hobby, interest, or fun fact. "In my free time, I enjoy..." "I'm passionate about..."

## Formal vs. Informal Introductions

**Formal** (interview, business): "Good morning. My name is Aliya Nurova. I'm a marketing specialist at TechCorp, where I manage our digital campaigns. I have five years of experience in digital marketing. It's a pleasure to meet you."

**Informal** (party, casual): "Hey, I'm Aliya! I work in marketing. I'm really into hiking and photography. Nice to meet you!"

**Networking event**: "Hi, I'm Aliya from TechCorp. I work on digital marketing strategy. I'm here because I'm interested in learning more about AI in marketing. What brings you here?"

## Responding to Introductions

"Nice to meet you." / "Pleased to meet you." / "Likewise." / "Great to meet you too."
If you did not catch the name: "Sorry, could you repeat your name?" "I didn't quite catch your name."

## Common Phrases for Expanding the Conversation

After introductions, keep the conversation going: "So, what do you do?" "Have you been here before?" "How do you know [host/organizer]?" "Where are you based?" "What do you think of the event so far?"

## Tips for Confidence

- Practice your introduction until it feels natural, not rehearsed.
- Make eye contact and smile.
- Speak at a moderate pace — rushing signals nervousness.
- Prepare a short version (10 seconds) and a longer version (30 seconds) for different situations.
- End with a question to show interest in the other person. People appreciate when you are curious about them.`,
    videos: [
      { title: "How to Introduce Yourself in English", url: "https://www.youtube.com/watch?v=oWJdHJVNbqw", duration: "10:30" },
      { title: "Self Introduction - Professional English", url: "https://www.youtube.com/watch?v=dR2MNKCw9lQ", duration: "13:45" },
    ],
    quiz: [
      {
        question: "What is the best response to 'Nice to meet you'?",
        options: ["Thank you.", "Nice to meet you too.", "You're welcome.", "I'm fine."],
        correct: 1,
      },
      {
        question: "Which is more appropriate for a job interview introduction?",
        options: [
          "Hey, I'm Alex, I like music.",
          "Good morning. My name is Alex. I'm a software engineer with five years of experience.",
          "What's up? Alex here.",
          "Hello, I am Alex, I want money.",
        ],
        correct: 1,
      },
    ],
  },

  "en-10-1": {
    id: "en-10-1",
    title: "Small Talk Practice",
    content: `# The Art of Small Talk

Small talk is light, casual conversation about non-controversial topics. It is the social glue that builds rapport and makes interactions comfortable. Mastering small talk is essential for both social and professional success in English-speaking environments.

## Why Small Talk Matters

Small talk is not meaningless chatter — it serves important social functions. It builds trust and rapport before discussing serious topics. It shows respect and interest in others. In business, deals are often influenced by the personal connection built through small talk before the meeting even starts.

## Safe Topics for Small Talk

**Weather**: "Beautiful day, isn't it?" "Can you believe this rain?" "Looks like it's going to warm up this week."
**Weekend/holidays**: "Do you have any plans for the weekend?" "How was your weekend?" "Did you do anything fun over the holiday?"
**Travel**: "Have you traveled anywhere recently?" "Any vacation plans coming up?"
**Food**: "Have you tried any good restaurants lately?" "Do you cook much?"
**Hobbies/interests**: "What do you like to do in your free time?" "Are you into any sports?"
**Current events (neutral)**: "Did you see that documentary about...?" "Have you heard about...?"

## Topics to Avoid

Politics, religion, salary/money, age, weight, personal problems, gossip about others, controversial social issues. These topics can make people uncomfortable and are generally considered inappropriate for light conversation.

## Techniques for Keeping Conversation Going

**Ask open-ended questions**: Instead of "Do you like your job?" (yes/no), ask "What do you enjoy most about your work?" This encourages longer, more detailed answers.

**Active listening**: "That sounds amazing!" "Really? Tell me more." "I didn't know that!" Show genuine interest through reactions and follow-up questions.

**Share related experiences**: "Oh, I've been there too! I loved the food." This creates connection and gives the other person something to respond to.

**The echo technique**: Repeat the last few words as a question. "I went to Japan last month." → "Japan? That must have been incredible! What was the highlight?"

## Ending a Conversation Gracefully

"Well, it was great chatting with you!" "I should get going, but it was lovely talking to you." "I'll let you get back to it — enjoy the rest of your day!" Always end positively, and if appropriate, suggest continuing: "We should grab coffee sometime."`,
    videos: [
      { title: "How to Make Small Talk in English", url: "https://www.youtube.com/watch?v=wXbPOEjZbqQ", duration: "14:20" },
      { title: "Small Talk Topics and Phrases", url: "https://www.youtube.com/watch?v=GHCIyStGJk0", duration: "11:50" },
    ],
    quiz: [
      {
        question: "Which topic is generally NOT appropriate for small talk?",
        options: ["Weather", "Weekend plans", "Salary", "Travel"],
        correct: 2,
      },
      {
        question: "Which is an open-ended question?",
        options: ["Do you like coffee?", "Is it raining?", "What do you enjoy most about your work?", "Did you go to the meeting?"],
        correct: 2,
      },
      {
        question: "What is the 'echo technique'?",
        options: [
          "Speaking loudly",
          "Repeating the other person's last words as a question",
          "Saying the same thing twice",
          "Mimicking someone's accent",
        ],
        correct: 1,
      },
    ],
  },

  "en-11-1": {
    id: "en-11-1",
    title: "Opinion Phrases",
    content: `# Expressing Opinions in English

Being able to express, support, and respond to opinions is crucial for meetings, discussions, essays, and everyday conversation. English has many nuanced ways to share your view — from tentative to strong.

## Giving Your Opinion

**Strong opinions**: "I strongly believe that..." "I'm convinced that..." "There's no doubt in my mind that..." "I firmly believe..."

**Moderate opinions**: "I think that..." "In my opinion..." "From my point of view..." "As I see it..." "It seems to me that..." "I'd say that..."

**Tentative/careful opinions**: "I tend to think that..." "I'm inclined to believe..." "If you ask me..." "I might be wrong, but..." "It could be that..."

## Agreeing with Others

**Strong agreement**: "I completely agree." "Absolutely!" "Exactly!" "That's exactly what I think." "I couldn't agree more."

**Partial agreement**: "I agree to some extent." "You have a point, but..." "I see what you mean, however..." "That's partly true." "I agree with you up to a point."

## Disagreeing Politely

Direct disagreement can sound rude in English. Use softening language:

**Polite disagreement**: "I see your point, but I think..." "I understand where you're coming from, however..." "I respect your opinion, but I have a different view." "That's an interesting perspective, but have you considered...?" "I'm not sure I agree with that."

**Stronger disagreement** (still professional): "I have to disagree on that point." "I don't think that's entirely accurate." "With all due respect, I see it differently."

**Avoid**: "You're wrong." "That's ridiculous." "That makes no sense." — These are considered impolite in professional and many social contexts.

## Supporting Your Opinion

Always back up your opinion with reasons: "I think remote work is effective because studies show productivity increases by 13%." Use phrases like: "The reason I say this is..." "Let me give you an example..." "For instance..." "Evidence suggests that..." "In my experience..."

## Asking for Opinions

"What do you think about...?" "What's your take on...?" "How do you feel about...?" "Do you have any thoughts on...?" "Where do you stand on...?" These phrases invite others into the discussion and show respect for their perspective.`,
    videos: [
      { title: "How to Express Your Opinion in English", url: "https://www.youtube.com/watch?v=7SyX80iBiWU", duration: "11:40" },
      { title: "Agreeing and Disagreeing Politely", url: "https://www.youtube.com/watch?v=YFqbMiXpMrs", duration: "13:25" },
    ],
    quiz: [
      {
        question: "Which phrase expresses a tentative opinion?",
        options: ["I'm certain that...", "There's no doubt that...", "I tend to think that...", "I strongly believe..."],
        correct: 2,
      },
      {
        question: "Which is a polite way to disagree?",
        options: ["You're wrong.", "That's ridiculous.", "I see your point, but I think...", "That makes no sense."],
        correct: 2,
      },
      {
        question: "What does 'I couldn't agree more' mean?",
        options: ["I disagree.", "I partially agree.", "I completely agree.", "I have no opinion."],
        correct: 2,
      },
    ],
  },

  "en-12-1": {
    id: "en-12-1",
    title: "Pronunciation",
    content: `# Pronunciation Practice: Stress, Intonation & Common Mistakes

Clear pronunciation is not about having a perfect accent — it is about being understood. Focus on stress, intonation, and the sounds that cause the most confusion.

## Word Stress

English words have stressed and unstressed syllables. Stressing the wrong syllable can make a word unrecognizable. Rules of thumb:

- **Two-syllable nouns**: stress the FIRST syllable — TAble, PREsent, REcord, OBject.
- **Two-syllable verbs**: stress the SECOND syllable — preSENT, reCORD, obJECT.
- **Words ending in -tion/-sion**: stress the syllable before — informATION, decISION, educATION.
- **Words ending in -ic**: stress the syllable before — fanTAStic, draMATic, scienTIFic.

Incorrect stress changes meaning: "REcord" (noun: a music record) vs. "reCORD" (verb: to record something). "PREsent" (noun: a gift) vs. "preSENT" (verb: to present).

## Sentence Stress

In English sentences, content words (nouns, main verbs, adjectives, adverbs) are stressed, while function words (articles, prepositions, auxiliary verbs, pronouns) are unstressed and often reduced: "I want to GO to the STORE to BUY some BREAD." The unstressed words blur together, creating English rhythm.

## Intonation Patterns

**Falling intonation** (pitch goes down at the end): statements and wh-questions. "I live in London. ↘" "Where do you work? ↘"

**Rising intonation** (pitch goes up at the end): yes/no questions. "Do you like coffee? ↗" "Are you coming? ↗"

**Rise-fall**: showing interest or surprise. "Really? ↗↘" "That's amazing! ↗↘"

## Common Pronunciation Mistakes

- **Silent letters**: k in "know," w in "write," b in "debt," l in "would/should/could," g in "sign."
- **th sounds**: Practice /θ/ ("think," "three") and /ð/ ("this," "the") — tongue between teeth.
- **-ed endings**: Three pronunciations: /t/ after voiceless sounds ("walked," "watched"), /d/ after voiced sounds ("played," "arrived"), /ɪd/ after t/d sounds ("wanted," "needed").
- **Vowel length**: "ship" vs. "sheep," "bit" vs. "beat," "full" vs. "fool" — length changes meaning.
- **Word-final consonants**: Do not drop them. "Hand" should not sound like "han." "World" should not sound like "worl."

## Practice Techniques

Read aloud for 10 minutes daily. Shadow native speakers — listen to a sentence, then immediately repeat it with the same rhythm and stress. Record yourself and compare. Use tongue twisters: "She sells seashells by the seashore." "Red lorry, yellow lorry."`,
    videos: [
      { title: "English Pronunciation - Word Stress Rules", url: "https://www.youtube.com/watch?v=DfKMFxraGhs", duration: "15:10" },
      { title: "Intonation in English - Rise and Fall", url: "https://www.youtube.com/watch?v=oCIgt2LVlKY", duration: "13:50" },
    ],
    quiz: [
      {
        question: "Where is the stress in the noun 'REcord'?",
        options: ["First syllable", "Second syllable", "Both syllables", "No stress"],
        correct: 0,
      },
      {
        question: "How is the '-ed' in 'wanted' pronounced?",
        options: ["/t/", "/d/", "/ɪd/", "It is silent"],
        correct: 2,
      },
      {
        question: "What intonation pattern do yes/no questions typically use?",
        options: ["Falling", "Rising", "Flat", "Rise-fall"],
        correct: 1,
      },
    ],
  },

  "en-13-1": {
    id: "en-13-1",
    title: "Business Emails",
    content: `# Professional Email Writing

Email is the primary communication tool in business. A well-written email is clear, professional, and action-oriented. Poorly written emails cause misunderstandings, waste time, and can damage professional relationships.

## Email Structure

Every professional email has these components:

1. **Subject line**: Clear and specific. "Meeting rescheduled to March 15" (NOT "Meeting"). "Q3 Marketing Report — Feedback Requested" (NOT "Report").
2. **Greeting**: "Dear Mr./Ms. [Last Name]," (formal). "Hi [First Name]," (semi-formal). "Hello [Name]," (neutral).
3. **Opening line**: State the purpose immediately. "I am writing to inquire about..." "I wanted to follow up on our conversation." "Thank you for your email regarding..."
4. **Body**: Keep it concise. One topic per email. Use short paragraphs and bullet points for clarity.
5. **Closing/call to action**: State what you need. "Could you please send the report by Friday?" "Please let me know if you have any questions."
6. **Sign-off**: "Best regards," "Kind regards," "Sincerely," "Thank you," followed by your name and title.

## Common Email Templates

**Requesting information**: "Dear Ms. Johnson, I hope this email finds you well. I am writing to request information about your training programs. Specifically, I would like to know: (1) available dates, (2) pricing, and (3) group discounts. I would appreciate it if you could send these details at your earliest convenience. Best regards, [Name]"

**Following up**: "Hi David, I wanted to follow up on the proposal I sent last Tuesday. Have you had a chance to review it? I would be happy to discuss any questions you might have. Looking forward to hearing from you. Best, [Name]"

**Apologizing**: "Dear Mr. Chen, I sincerely apologize for the delay in delivering the report. This was due to unforeseen technical issues. The report is now complete and attached. I will ensure this does not happen again. Kind regards, [Name]"

## Professional Email Etiquette

- Reply within 24 hours, even if just to acknowledge receipt.
- Use "Reply All" sparingly — only when everyone needs the information.
- Proofread before sending. Check names, dates, and attachments.
- Avoid ALL CAPS (reads as shouting), excessive exclamation marks, and emojis in formal emails.
- Be careful with tone — humor and sarcasm often do not translate well in writing.
- "Please find attached" is the standard phrase for sending files (NOT "I am attaching" or "Attached herewith").

## Useful Phrases

**Opening**: "I hope this email finds you well." "Thank you for your prompt reply." "Further to our meeting yesterday..."
**Requesting**: "Could you please...?" "I would appreciate it if..." "Would it be possible to...?"
**Offering help**: "Please do not hesitate to contact me." "I would be happy to assist."
**Closing**: "I look forward to hearing from you." "Thank you for your time and consideration." "Please let me know if you need any further information."`,
    videos: [
      { title: "How to Write Professional Emails in English", url: "https://www.youtube.com/watch?v=eDmDiJJz1JE", duration: "16:40" },
      { title: "Business Email Writing Tips", url: "https://www.youtube.com/watch?v=JXCcPDZOgS4", duration: "12:30" },
    ],
    quiz: [
      {
        question: "What makes a good email subject line?",
        options: ["Just 'Hello'", "As long as possible", "Clear and specific about the topic", "All capital letters"],
        correct: 2,
      },
      {
        question: "Which is the standard phrase for sending attached files?",
        options: ["I'm giving you the file.", "Here is the file.", "Please find attached...", "Take this file."],
        correct: 2,
      },
      {
        question: "Which sign-off is appropriate for a professional email?",
        options: ["Cheers mate,", "Best regards,", "Bye bye,", "XOXO,"],
        correct: 1,
      },
    ],
  },

  "en-14-1": {
    id: "en-14-1",
    title: "Meeting Language",
    content: `# Vocabulary and Phrases for Meetings & Calls

Meetings are a core part of professional life. Knowing the right phrases for each stage of a meeting helps you participate confidently and effectively.

## Starting a Meeting

**Chair/host**: "Let's get started, shall we?" "Thank you all for joining today." "The purpose of today's meeting is to..." "Let's begin with the first item on the agenda."
**Participant**: "Thanks for having me." "Happy to be here."

## Setting the Agenda

"There are three items on today's agenda." "First, we'll discuss... Then we'll move on to... Finally, we'll cover..." "Does anyone want to add anything to the agenda?"

## Giving Your Input

"I'd like to share my thoughts on this." "If I may add something..." "From our team's perspective..." "Based on the data, I think..." "Can I jump in here?" (to interrupt politely)

## Asking for Clarification

"Could you elaborate on that?" "What exactly do you mean by...?" "Sorry, I didn't quite catch that. Could you repeat it?" "Just to clarify, are you saying that...?" "Could you give us an example?"

## Managing Discussion

"Let's stay on topic." "We're running short on time." "Can we come back to this point later?" "Let's table this for now and move on." "I think we've covered this. Shall we move to the next item?"

## Making Decisions & Action Items

"So, to summarize what we've agreed on..." "The next steps are..." "[Name] will take care of [task] by [deadline]." "Let's set a deadline for this — how about next Friday?" "Who wants to take the lead on this?"

## Closing a Meeting

"That covers everything on the agenda." "Thank you all for your time." "I'll send out the meeting minutes by end of day." "Our next meeting is scheduled for..." "If there are no further questions, let's wrap up."

## Phone & Video Call Phrases

**Technical issues**: "Can you hear me?" "You're breaking up." "Let me try reconnecting." "Could you turn on your camera?" "I'll share my screen now."
**Joining late**: "Sorry I'm late. What did I miss?" "Apologies for joining late."
**Muting**: "You're on mute." "Let me unmute myself." "Please mute yourselves when not speaking."

## Conference Call Etiquette

Mute when not speaking. Identify yourself before speaking on large calls: "This is [Name] — I just wanted to say..." Avoid multitasking visibly. Be punctual — join 1-2 minutes early for important calls.`,
    videos: [
      { title: "English for Meetings - Useful Phrases", url: "https://www.youtube.com/watch?v=OagPOdVp0_0", duration: "15:20" },
      { title: "Business English - Conference Calls", url: "https://www.youtube.com/watch?v=9pOyEX3Sm_Q", duration: "12:10" },
    ],
    quiz: [
      {
        question: "How do you politely interrupt someone in a meeting?",
        options: ["Stop talking.", "Can I jump in here?", "Be quiet.", "I don't care about your point."],
        correct: 1,
      },
      {
        question: "What does 'Let's table this' mean?",
        options: ["Put it on the table", "Discuss it in detail now", "Postpone it for later", "Cancel it entirely"],
        correct: 2,
      },
      {
        question: "What should you say when joining a video call late?",
        options: ["I'm here now.", "Sorry I'm late. What did I miss?", "Start over for me.", "Whatever."],
        correct: 1,
      },
    ],
  },

  "en-15-1": {
    id: "en-15-1",
    title: "Presentation Skills",
    content: `# Delivering Presentations in English

Presentations are a high-visibility opportunity to demonstrate both your expertise and your English communication skills. A well-structured presentation follows a clear pattern that the audience can easily follow.

## Presentation Structure

**Opening (10%)**: Greet, introduce yourself, state the topic, outline the structure, and hook the audience.
**Body (80%)**: Present your main points with supporting evidence, examples, and visuals.
**Conclusion (10%)**: Summarize key takeaways, make a call to action, and open for Q&A.

## Opening Phrases

"Good morning/afternoon everyone. My name is [Name] and I'm here today to talk about..."
"Thank you for being here. Today I'd like to present our findings on..."
"Before I begin, let me give you a brief overview of what I'll cover today."
"I've divided my presentation into three parts. First... Second... And finally..."
"Let me start with a question: How many of you have experienced...?"

## Transitioning Between Sections

"Now let's move on to..." "That brings me to my next point..." "Having looked at [topic 1], let's now turn to [topic 2]." "So, that's the background. Now, what does this mean in practice?" "As you can see from this slide..."

## Presenting Data & Visuals

"As you can see from this chart..." "This graph shows a clear trend in..." "If you look at the figures, you'll notice that..." "The key takeaway from this data is..." "Let me draw your attention to..."

## Engaging the Audience

"Has anyone here experienced this?" "Let me give you a real-world example." "Imagine you're in a situation where..." "Think about the last time you..." "I'd like to share a brief story."

## Concluding Your Presentation

"To summarize the main points..." "In conclusion, I'd like to emphasize three things." "The key message I want you to take away is..." "Thank you for your attention. I'd be happy to take any questions now." "Does anyone have any questions or comments?"

## Handling Q&A

"That's a great question." "Let me address that." "I'm glad you brought that up." "If I understand your question correctly, you're asking about..." "I don't have that information right now, but I'll follow up with you after the session."

**If you don't understand a question**: "Could you rephrase that?" "I'm not sure I follow — could you be more specific?" These are perfectly acceptable responses.

## Delivery Tips

Speak slowly and clearly — nerves make us speed up. Use pauses for emphasis — silence is powerful. Maintain eye contact with different sections of the audience. Use gestures naturally. Practice your opening and closing until they feel effortless. Time your presentation in advance.`,
    videos: [
      { title: "How to Give a Presentation in English", url: "https://www.youtube.com/watch?v=x8qiUNaRPBQ", duration: "18:00" },
      { title: "Presentation Phrases - Business English", url: "https://www.youtube.com/watch?v=Ub0vV-v-bXQ", duration: "14:40" },
    ],
    quiz: [
      {
        question: "What percentage of a presentation should the body typically take?",
        options: ["50%", "60%", "70%", "80%"],
        correct: 3,
      },
      {
        question: "What should you say if you don't understand a question during Q&A?",
        options: ["That's a stupid question.", "Could you rephrase that?", "I don't want to answer.", "Ask someone else."],
        correct: 1,
      },
    ],
  },

  "en-16-1": {
    id: "en-16-1",
    title: "Negotiation Language",
    content: `# Negotiation Language in English

Negotiation is a collaborative process of reaching an agreement. In English-speaking business cultures, effective negotiation relies on clear communication, assertiveness combined with politeness, and strategic use of language.

## Key Negotiation Phrases

**Opening positions**: "We'd like to propose..." "Our initial offer is..." "What we have in mind is..." "We're looking for a solution that works for both sides."

**Making concessions**: "We could consider..." "We'd be willing to [offer] if you could [condition]." "We could meet you halfway." "We're prepared to be flexible on [point] if..."

**Requesting concessions**: "Would you be able to...?" "Is there any room for flexibility on...?" "Could you improve your offer on...?" "What if we adjusted the terms to include...?"

**Expressing limits**: "I'm afraid that's beyond what we can offer." "That's not something we can agree to." "We've reached our limit on this point." "Unfortunately, we can't go any further than..."

## Negotiation Strategies in English

**Win-win framing**: "How can we make this work for both of us?" "Let's find a solution that benefits everyone." This collaborative approach is valued in many English-speaking business cultures.

**Conditional offers (If... then...)**: "If you can commit to a two-year contract, then we can offer a 15% discount." "We'd be happy to extend the warranty if you increase the order volume." This structure keeps negotiations balanced.

**Silence**: After making an offer, stop talking. Let the other side respond. Many negotiators fill silence with concessions they did not need to make.

## Bargaining and Compromise

"Let's split the difference." "Can we find a middle ground?" "What would it take for you to agree to this?" "We're close — let's see if we can bridge the gap." "I think we can work something out."

## Closing the Deal

"I think we have a deal." "Let's put this in writing." "Shall we shake on it?" "I'm happy with these terms." "I'll have our legal team draft the contract." "Let's confirm the key points we've agreed on."

## Handling Difficult Moments

"Let's take a step back and look at the bigger picture." "I suggest we take a short break." "Let's focus on what we agree on." "I understand your concern, and here's how we can address it." "Let's not let this one issue derail the entire negotiation."

## Cultural Considerations

In many English-speaking cultures, negotiations tend to be direct but polite. Avoid aggressive language or ultimatums. Building personal rapport is important — some small talk before diving into business is expected. "No" is often softened: "That might be difficult" or "We'd need to think about that" frequently means no.`,
    videos: [
      { title: "Business English - Negotiation Skills", url: "https://www.youtube.com/watch?v=KhfkKAUiJiI", duration: "16:30" },
      { title: "Negotiation Phrases in English", url: "https://www.youtube.com/watch?v=jOJvUJWPuno", duration: "14:15" },
    ],
    quiz: [
      {
        question: "What does 'Let's split the difference' mean?",
        options: ["End the negotiation", "Each side gives up half the gap", "Take a break", "Start over"],
        correct: 1,
      },
      {
        question: "Which is a good conditional offer structure?",
        options: [
          "Give us a discount or we leave.",
          "If you extend the warranty, we'll increase the order.",
          "We want everything cheaper.",
          "Take it or leave it.",
        ],
        correct: 1,
      },
      {
        question: "In English-speaking business culture, 'That might be difficult' often means:",
        options: ["It's possible", "They need more time", "No", "They are enthusiastic"],
        correct: 2,
      },
    ],
  },

  "en-17-1": {
    id: "en-17-1",
    title: "Advanced Grammar",
    content: `# Advanced Grammar: Conditionals, Passive Voice & Reported Speech

These three grammar topics are essential for upper-intermediate and advanced English. They allow you to express hypothetical situations, describe processes, and relay what others have said.

## Conditional Sentences

**Zero Conditional** (general truths): If + present simple, present simple. "If you heat water to 100°C, it boils." Always true.

**First Conditional** (real future possibility): If + present simple, will + base verb. "If it rains tomorrow, I will stay home." Likely or possible.

**Second Conditional** (unreal/unlikely present or future): If + past simple, would + base verb. "If I won the lottery, I would travel the world." Hypothetical — I probably won't win. Note: "If I were you" (NOT "was") is the traditional form.

**Third Conditional** (unreal past — regret/imagination): If + past perfect, would have + past participle. "If I had studied harder, I would have passed the exam." It's too late — it didn't happen.

**Mixed Conditional**: Combines second and third. "If I had accepted that job (past), I would be living in New York now (present)."

## Passive Voice

Use passive when the action is more important than who did it, when the doer is unknown, or in formal/scientific writing.

**Form**: Subject + be + past participle (+ by agent).
- "The report was written by the team." (passive) vs. "The team wrote the report." (active)
- "English is spoken worldwide." (no agent needed)
- "The building was constructed in 1985." (agent unknown/unimportant)

**Tense examples**: "The email is being sent now." (present continuous passive) "The project has been completed." (present perfect passive) "A decision will be made tomorrow." (future passive)

## Reported Speech

When you relay what someone said, you shift tenses back:

- Present simple → Past simple: She said, "I work here" → She said she worked there.
- Present continuous → Past continuous: "I am leaving" → He said he was leaving.
- Past simple → Past perfect: "I saw him" → She said she had seen him.
- Will → Would: "I will call you" → He said he would call me.
- Can → Could: "I can help" → She said she could help.

**Reporting verbs**: said, told, explained, mentioned, claimed, admitted, denied, suggested, warned, promised. "She told me she was busy." "He explained that the project was delayed." "They warned us that it would be difficult."

**Time/place changes**: now → then, today → that day, yesterday → the day before, tomorrow → the next day, here → there, this → that.

## Common Mistakes

- Forgetting to backshift tenses in reported speech.
- Using "was" instead of "were" in second conditional with I/he/she/it.
- Confusing active and passive: "The mistake made by me" should be "The mistake was made by me."`,
    videos: [
      { title: "Conditional Sentences - All Types Explained", url: "https://www.youtube.com/watch?v=m-MHo4HBi-0", duration: "18:40" },
      { title: "Passive Voice - Complete Guide", url: "https://www.youtube.com/watch?v=S7rIxRKXfOA", duration: "15:25" },
      { title: "Reported Speech Made Easy", url: "https://www.youtube.com/watch?v=xjXjjMNTleo", duration: "14:50" },
    ],
    quiz: [
      {
        question: "Which conditional is used for unreal past situations?",
        options: ["Zero", "First", "Second", "Third"],
        correct: 3,
      },
      {
        question: "Convert to passive: 'Someone stole my bike.'",
        options: ["My bike stolen.", "My bike was stolen.", "My bike is stolen.", "My bike has stolen."],
        correct: 1,
      },
      {
        question: "Report: She said, 'I am tired.' →",
        options: [
          "She said she is tired.",
          "She said she was tired.",
          "She said she will be tired.",
          "She said she has been tired.",
        ],
        correct: 1,
      },
    ],
  },

  "en-18-1": {
    id: "en-18-1",
    title: "Debate Skills",
    content: `# Debate & Argumentation in English

Debate is the art of constructing and defending arguments logically and persuasively. It sharpens your critical thinking and your ability to communicate complex ideas under pressure.

## Building an Argument

A strong argument has three parts:

1. **Claim**: Your main point. "Remote work increases productivity."
2. **Evidence**: Facts, statistics, or examples that support your claim. "A Stanford study found that remote workers were 13% more productive than office workers."
3. **Reasoning**: The logical connection between your evidence and claim. "This is because remote workers face fewer distractions and save commuting time, allowing them to focus more on tasks."

## Argument Phrases

**Stating your position**: "I would argue that..." "The evidence clearly shows that..." "It is undeniable that..." "The main reason I support this is..."

**Providing evidence**: "According to research by..." "Statistics show that..." "A recent study found that..." "For example..." "To illustrate this point..."

**Strengthening your argument**: "Furthermore..." "Moreover..." "In addition to this..." "Not only... but also..." "This is further supported by the fact that..."

## Counterarguments

Acknowledging and refuting opposing views makes your argument stronger:

"Some people might argue that [opposing view]. However, [your response]."
"While it is true that [concession], this does not negate the fact that [your point]."
"Critics may point to [counter evidence], but this overlooks [your evidence]."
"Although [opposing view] has some merit, the weight of evidence suggests..."

## Logical Fallacies to Avoid

- **Ad hominem**: Attacking the person instead of the argument. "You're too young to understand."
- **Straw man**: Misrepresenting someone's argument to make it easier to attack.
- **False dichotomy**: Presenting only two options when more exist. "You're either with us or against us."
- **Appeal to authority**: Using someone's status rather than evidence. "It must be true because a celebrity said it."
- **Slippery slope**: Assuming one thing will inevitably lead to an extreme outcome.

## Debate Etiquette

Listen actively to your opponent. Address their points directly rather than ignoring them. Stay calm and professional — never raise your voice or become personal. Use phrases like "With respect, I disagree" rather than "You're wrong." Admit when the other side makes a good point — it shows intellectual honesty and actually strengthens your credibility.

## Concluding an Argument

"In light of the evidence presented..." "To sum up my position..." "The key takeaway is..." "Given all of these factors, it is clear that..." "I rest my case."`,
    videos: [
      { title: "How to Argue Effectively in English", url: "https://www.youtube.com/watch?v=vlIGNrCWcqA", duration: "14:30" },
      { title: "Critical Thinking and Debate Skills", url: "https://www.youtube.com/watch?v=Cum3k7Do-oU", duration: "17:15" },
    ],
    quiz: [
      {
        question: "What are the three parts of a strong argument?",
        options: [
          "Greeting, body, conclusion",
          "Claim, evidence, reasoning",
          "Introduction, discussion, summary",
          "Opinion, example, question",
        ],
        correct: 1,
      },
      {
        question: "What is an 'ad hominem' fallacy?",
        options: [
          "Using unreliable statistics",
          "Attacking the person instead of the argument",
          "Presenting only two options",
          "Appealing to emotion",
        ],
        correct: 1,
      },
      {
        question: "Why should you acknowledge counterarguments?",
        options: [
          "To weaken your position",
          "To confuse the audience",
          "It makes your argument stronger",
          "It's required by law",
        ],
        correct: 2,
      },
    ],
  },

  "en-19-1": {
    id: "en-19-1",
    title: "Interview Prep",
    content: `# English for Job Interviews

A job interview in English requires both language skills and strategic preparation. This lesson covers the most common questions, ideal answer structures, and essential phrases.

## Before the Interview

Research the company thoroughly. Prepare answers to common questions. Practice out loud — not just in your head. Prepare your own questions for the interviewer. Test your technology if it's a video interview.

## Common Interview Questions & How to Answer

**"Tell me about yourself."**
Use the Present-Past-Future formula: "I'm currently a [role] at [company], where I [main responsibility]. Before that, I worked at [previous company], where I [achievement]. I'm now looking for an opportunity to [goal] — which is why I'm excited about this role."

**"What are your strengths?"**
Choose 2-3 strengths relevant to the role, with brief examples: "One of my key strengths is problem-solving. For example, at my previous job, I identified a workflow issue that was costing us 10 hours per week, and I implemented a solution that eliminated it."

**"What is your greatest weakness?"**
Be honest but strategic. Choose a real weakness, then show what you're doing about it: "I used to struggle with delegating tasks. I tended to take on too much myself. I've been working on this by actively assigning tasks to team members and trusting their capabilities, which has improved our team's efficiency."

**"Why do you want to work here?"**
Show genuine interest and research: "I've been following your company's work in [area], and I'm impressed by [specific thing]. My skills in [relevant skill] align well with your goals of [company goal], and I believe I can make a meaningful contribution."

**"Where do you see yourself in five years?"**
Show ambition aligned with the company: "I see myself growing into a senior role where I can lead projects and mentor junior team members, while continuing to develop my expertise in [field]."

## The STAR Method for Behavioral Questions

When asked "Tell me about a time when..." use STAR:
- **S**ituation: Set the scene briefly.
- **T**ask: What was your responsibility?
- **A**ction: What did you do specifically?
- **R**esult: What was the outcome? Use numbers if possible.

Example: "In my previous role (Situation), I was asked to increase our social media engagement (Task). I developed a content calendar and introduced video content (Action). Within three months, engagement increased by 45% (Result)."

## Questions to Ask the Interviewer

"What does a typical day look like in this role?" "What are the biggest challenges facing the team right now?" "How do you measure success in this position?" "What opportunities for professional development do you offer?" "What are the next steps in the hiring process?"

## Closing the Interview

"Thank you for your time. I really enjoyed our conversation." "I'm very excited about this opportunity." "I look forward to hearing from you." Send a thank-you email within 24 hours reiterating your interest.`,
    videos: [
      { title: "Job Interview Tips - How to Answer Common Questions", url: "https://www.youtube.com/watch?v=kayOhGRcNt4", duration: "17:45" },
      { title: "STAR Method - Behavioral Interview Answers", url: "https://www.youtube.com/watch?v=WSbN-0swDgM", duration: "13:20" },
    ],
    quiz: [
      {
        question: "What does the STAR method stand for?",
        options: [
          "Start, Try, Assess, Review",
          "Situation, Task, Action, Result",
          "Strengths, Threats, Aims, Resources",
          "Subject, Topic, Answer, Reason",
        ],
        correct: 1,
      },
      {
        question: "When answering 'What is your weakness?', you should:",
        options: [
          "Say you have no weaknesses",
          "Name a real weakness and what you're doing to improve",
          "Name a strength disguised as a weakness",
          "Avoid the question",
        ],
        correct: 1,
      },
      {
        question: "What should you do within 24 hours after an interview?",
        options: ["Call the interviewer", "Send a thank-you email", "Apply to other jobs", "Post about it on social media"],
        correct: 1,
      },
    ],
  },

  "en-20-1": {
    id: "en-20-1",
    title: "Cultural Context",
    content: `# Cultural Fluency in English

Language and culture are inseparable. Understanding the cultural context behind English communication helps you avoid misunderstandings and connect more effectively with English speakers from different backgrounds.

## Direct vs. Indirect Communication

**American English** tends to be more direct: "I disagree." "That won't work." "I need this by Friday." Americans often value getting to the point quickly.

**British English** tends to be more indirect: "I'm not sure that's quite right." "That's an interesting idea" (may mean "I disagree"). "It would be great if we could have this by Friday" (means "I need this by Friday"). Understanding British understatement is crucial — "That's not bad" often means "That's quite good."

**Australian English** is generally informal and uses humor frequently. "No worries" means "you're welcome" or "it's fine." Australians tend to use irony and self-deprecation in conversation.

## Politeness Conventions

English speakers, especially in professional settings, use extensive softening language:
- "Would you mind...?" instead of "Do this."
- "I was wondering if..." instead of "Can you...?"
- "Could you possibly...?" instead of "You need to..."
- "I'm afraid I can't..." instead of "No."
- "That might be a bit challenging" instead of "That's impossible."

Directness that is normal in many cultures can sound rude in English. When in doubt, be more polite than you think is necessary.

## Humor in English

Humor plays a significant role in English communication, including in business. Sarcasm, irony, and self-deprecating humor are common, especially in British English. "Oh great, another meeting" (sarcasm — the speaker is not actually pleased). "I'm terrible at this" (self-deprecation — the speaker may actually be quite skilled). If you are unsure whether someone is being sarcastic, look at their tone, facial expression, and context.

## Cultural Topics and Taboos

**Safe conversation topics**: weather, sports, travel, food, entertainment, pets, weekend plans.
**Handle with care**: politics (especially in mixed company), religion, income, age, weight.
**Workplace culture**: In many English-speaking countries, work-life balance is valued. Asking someone "Why aren't you married?" or "How old are you?" is considered intrusive. Personal space is important — maintain about an arm's length distance in conversation.

## Idioms with Cultural Roots

Many English idioms come from sports, history, and culture: "The ball is in your court" (tennis). "Touch base" (baseball). "Move the goalposts" (football/soccer). "Level playing field" (sports in general). "Break a leg" (theater — means "good luck"). Understanding these origins helps you remember and use them correctly.

## Tips for Cultural Fluency

- Watch English TV shows, films, and podcasts from different English-speaking countries to absorb cultural norms.
- Pay attention to how native speakers respond to compliments, criticism, and requests.
- When in doubt, observe before participating — watch how others behave in social and professional settings.
- Ask clarifying questions: "I want to make sure I understand — are you saying...?" This is always appropriate and shows good communication skills.
- Remember that "How are you?" is usually a greeting, not a genuine question — the expected answer is "Fine, thanks" or "Good, and you?"`,
    videos: [
      { title: "British vs American English - Key Differences", url: "https://www.youtube.com/watch?v=MBFsPEVRxys", duration: "16:50" },
      { title: "English Cultural Tips for Non-Native Speakers", url: "https://www.youtube.com/watch?v=Osqf4oIK0E8", duration: "13:30" },
    ],
    quiz: [
      {
        question: "In British English, 'That's an interesting idea' in a meeting often means:",
        options: ["They love the idea", "They want to hear more", "They probably disagree", "They have no opinion"],
        correct: 2,
      },
      {
        question: "What is the expected response to 'How are you?' as a greeting?",
        options: [
          "A detailed description of your day",
          "Fine, thanks. And you?",
          "I have many problems.",
          "Why do you ask?",
        ],
        correct: 1,
      },
      {
        question: "Which topic is generally considered inappropriate to discuss with colleagues?",
        options: ["Weekend plans", "Travel experiences", "Personal income", "A new restaurant"],
        correct: 2,
      },
    ],
  },
};
