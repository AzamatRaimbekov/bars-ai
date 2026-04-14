import { useState, useEffect, useCallback } from "react";
import { t, getLanguage, setLanguage, type Lang, type TranslationKey } from "@/lib/i18n";

export function useTranslation() {
  const [lang, setLang] = useState<Lang>(getLanguage());

  useEffect(() => {
    const handler = () => setLang(getLanguage());
    window.addEventListener("lang-change", handler);
    return () => window.removeEventListener("lang-change", handler);
  }, []);

  const changeLanguage = useCallback((newLang: Lang) => {
    setLanguage(newLang);
    setLang(newLang);
  }, []);

  const translate = useCallback(
    (key: TranslationKey, params?: Record<string, string>) => t(key, params),
    // eslint-disable-next-line react-hooks/exhaustive-deps
    [lang]
  );

  return { t: translate, lang, changeLanguage };
}
