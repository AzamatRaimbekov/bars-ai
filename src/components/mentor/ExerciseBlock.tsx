import { useState } from "react";
import { motion } from "framer-motion";
import { Send, CheckCircle, XCircle, MessageSquare, Code, Users } from "lucide-react";
import { Button } from "@/components/ui/Button";

interface ExerciseBlockProps {
  content: string;
  onSubmit: (answer: string) => void;
}

interface ParsedExercise {
  type: "code" | "qa" | "roleplay";
  body: string;
}

interface ParsedResult {
  score: string;
  feedback: string;
}

function parseExercises(content: string): {
  text: string;
  exercises: ParsedExercise[];
  results: ParsedResult[];
} {
  const exercises: ParsedExercise[] = [];
  const results: ParsedResult[] = [];

  // Parse [EXERCISE:type]...[/EXERCISE] blocks
  let text = content.replace(
    /\[EXERCISE:(code|qa|roleplay)\]([\s\S]*?)\[\/EXERCISE\]/g,
    (_match, type: string, body: string) => {
      exercises.push({ type: type as ParsedExercise["type"], body: body.trim() });
      return "";
    }
  );

  // Parse [EXERCISE_RESULT]...[/EXERCISE_RESULT] blocks
  text = text.replace(
    /\[EXERCISE_RESULT\]([\s\S]*?)\[\/EXERCISE_RESULT\]/g,
    (_match, body: string) => {
      const scoreMatch = body.match(/(?:score|оценка)[:\s]*(\d+[^\n]*)/i);
      const score = scoreMatch ? scoreMatch[1].trim() : "";
      const feedback = body
        .replace(/(?:score|оценка)[:\s]*\d+[^\n]*/i, "")
        .trim();
      results.push({ score, feedback });
      return "";
    }
  );

  return { text: text.trim(), exercises, results };
}

function ExerciseCodeInput({ body, onSubmit }: { body: string; onSubmit: (answer: string) => void }) {
  const [answer, setAnswer] = useState("");

  return (
    <div className="my-3 rounded-xl border border-primary/20 bg-primary/5 p-4">
      <div className="flex items-center gap-2 mb-3">
        <Code size={16} className="text-primary" />
        <span className="text-xs font-semibold text-primary uppercase tracking-wide">
          Задание: код
        </span>
      </div>
      <p className="text-sm text-text mb-3 whitespace-pre-wrap">{body}</p>
      <textarea
        value={answer}
        onChange={(e) => setAnswer(e.target.value)}
        placeholder="Напишите код здесь..."
        className="w-full h-32 bg-[#0A0A0A] border border-white/10 rounded-lg px-4 py-3 text-sm text-text font-mono outline-none focus:border-primary/40 resize-none placeholder:text-text-secondary/50"
      />
      <div className="flex justify-end mt-2">
        <Button
          size="sm"
          onClick={() => {
            if (answer.trim()) onSubmit(answer.trim());
          }}
          disabled={!answer.trim()}
        >
          <Send size={14} />
          Отправить
        </Button>
      </div>
    </div>
  );
}

function ExerciseQAInput({ body, onSubmit }: { body: string; onSubmit: (answer: string) => void }) {
  const [answer, setAnswer] = useState("");

  return (
    <div className="my-3 rounded-xl border border-accent/20 bg-accent/5 p-4">
      <div className="flex items-center gap-2 mb-3">
        <MessageSquare size={16} className="text-accent" />
        <span className="text-xs font-semibold text-accent uppercase tracking-wide">
          Вопрос
        </span>
      </div>
      <p className="text-sm text-text mb-3 whitespace-pre-wrap">{body}</p>
      <div className="flex gap-2">
        <input
          value={answer}
          onChange={(e) => setAnswer(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter" && answer.trim()) onSubmit(answer.trim());
          }}
          placeholder="Ваш ответ..."
          className="flex-1 bg-[#0A0A0A] border border-white/10 rounded-lg px-4 py-2.5 text-sm text-text outline-none focus:border-accent/40 placeholder:text-text-secondary/50"
        />
        <Button
          size="sm"
          onClick={() => {
            if (answer.trim()) onSubmit(answer.trim());
          }}
          disabled={!answer.trim()}
        >
          <Send size={14} />
        </Button>
      </div>
    </div>
  );
}

function ExerciseRoleplay({ body }: { body: string }) {
  return (
    <div className="my-3 rounded-xl border border-purple-500/20 bg-purple-500/5 p-4">
      <div className="flex items-center gap-2 mb-3">
        <Users size={16} className="text-purple-400" />
        <span className="text-xs font-semibold text-purple-400 uppercase tracking-wide">
          Ролевая игра
        </span>
      </div>
      <p className="text-sm text-text whitespace-pre-wrap">{body}</p>
    </div>
  );
}

function ExerciseResultBadge({ result }: { result: ParsedResult }) {
  const scoreNum = parseInt(result.score, 10);
  const isGood = !isNaN(scoreNum) ? scoreNum >= 7 : true;

  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      className={`my-3 rounded-xl border p-4 ${
        isGood
          ? "border-green-500/20 bg-green-500/5"
          : "border-red-500/20 bg-red-500/5"
      }`}
    >
      <div className="flex items-center gap-2 mb-2">
        {isGood ? (
          <CheckCircle size={16} className="text-green-400" />
        ) : (
          <XCircle size={16} className="text-red-400" />
        )}
        {result.score && (
          <span
            className={`text-xs font-bold px-2 py-0.5 rounded-full ${
              isGood
                ? "bg-green-500/20 text-green-300"
                : "bg-red-500/20 text-red-300"
            }`}
          >
            {result.score}
          </span>
        )}
      </div>
      {result.feedback && (
        <p className="text-sm text-text-secondary whitespace-pre-wrap">
          {result.feedback}
        </p>
      )}
    </motion.div>
  );
}

export function ExerciseBlock({ content, onSubmit }: ExerciseBlockProps) {
  const { text, exercises, results } = parseExercises(content);

  if (exercises.length === 0 && results.length === 0) {
    return <span>{content}</span>;
  }

  return (
    <div>
      {text && <p className="text-sm text-text whitespace-pre-wrap">{text}</p>}

      {exercises.map((ex, i) => {
        switch (ex.type) {
          case "code":
            return <ExerciseCodeInput key={i} body={ex.body} onSubmit={onSubmit} />;
          case "qa":
            return <ExerciseQAInput key={i} body={ex.body} onSubmit={onSubmit} />;
          case "roleplay":
            return <ExerciseRoleplay key={i} body={ex.body} />;
          default:
            return null;
        }
      })}

      {results.map((res, i) => (
        <ExerciseResultBadge key={`result-${i}`} result={res} />
      ))}
    </div>
  );
}
