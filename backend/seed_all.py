"""Run ALL seed scripts to populate the database with all courses."""
import asyncio
import importlib
import traceback
import sys
import os

sys.stdout.reconfigure(line_buffering=True)

# All seed modules in order: production first, then individual courses
SEED_MODULES = [
    "seed_production",
    "seed_ai_chatgpt",
    "seed_blender_3d",
    "seed_callcenter_course",
    "seed_chinese_language",
    "seed_claude_code_advanced",
    "seed_claude_code_course",
    "seed_claude_code_full",
    "seed_copywriting",
    "seed_cybersecurity",
    "seed_data_science",
    "seed_devops_course",
    "seed_dj_course",
    "seed_english_course",
    "seed_excel_course",
    "seed_finance_course",
    "seed_french_language",
    "seed_golang",
    "seed_graphic_design",
    "seed_kazakh_language",
    "seed_korean_language",
    "seed_kyrgyz_language",
    "seed_linux_admin",
    "seed_marketplace",
    "seed_nocode",
    "seed_photography",
    "seed_popping_course",
    "seed_product_management",
    "seed_python_course",
    "seed_qa_testing",
    "seed_react_native",
    "seed_sales_course",
    "seed_senior_frontend",
    "seed_soft_skills",
    "seed_spanish_language",
    "seed_sql_course",
    "seed_startup_course",
    "seed_targeted_ads",
    "seed_turkish_language",
    "seed_uiux_design",
    "seed_vibecoding_course",
    "seed_video_editing",
]


async def run_all():
    ok, fail = 0, 0
    for mod_name in SEED_MODULES:
        try:
            mod = importlib.import_module(mod_name)
            fn = getattr(mod, "main", None) or getattr(mod, "seed", None)
            if fn is None:
                print(f"  SKIP {mod_name}: no main() or seed()")
                continue
            print(f"  SEED {mod_name}...")
            await fn()
            ok += 1
        except Exception as e:
            print(f"  FAIL {mod_name}: {e}")
            traceback.print_exc()
            fail += 1
    print(f"\nSeed done: {ok} OK, {fail} failed, {len(SEED_MODULES)} total")
    sys.stdout.flush()


if __name__ == "__main__":
    asyncio.run(run_all())
