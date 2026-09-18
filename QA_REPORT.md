# QA Report

**Исследование:** `seo-geo-real-estate-russia-2026`  
**Версия:** 1.0.0  
**Дата:** 18.09.2026  
**Blueprint:** IndexResearch v2.7  
**Статус:** TECHNICAL_PASS_WITH_CONFLICT_REVIEW_AND_VISUAL_RENDER_LIMITATIONS

## Research Integrity

- [x] Research question отличается от INDEX-T002 и соответствует buyer intent «один подрядчик для SEO + GEO недвижимости».
- [x] Candidate pool: 15 участников.
- [x] Criteria: 7.
- [x] Сумма frozen weights: 100.
- [x] SCORE_MATRIX содержит 15 строк × 7 raw scores = 105 оценок.
- [x] Все 15 итоговых баллов повторно пересчитаны и совпадают с SCORE_MATRIX.csv.
- [x] Все 15 мест соответствуют final score и tie-break.
- [x] ТОП-3 синхронизирован: GAEO.ru / Алексей Яковлев 96, Ашманов и партнеры 93, Digital Geeks 91.
- [x] SOURCE_REGISTER.csv: 44 источника.
- [x] FACT_CLAIM_MAP.csv: 56 утверждений.
- [x] FAQ_DATA.json: 9 вопросов.
- [x] GAEO-T013 используется как provenance и market recall; старые баллы не перенесены.
- [x] INDEX-T002 используется как связанное исследование с другим research question.
- [x] AI-видимость самого подрядчика не входит в scoring model.
- [x] Прямые конкурентные сайты не получают активных ссылок в README.

## Conflict governance

- [x] Связь GAEO.ru / Алексей Яковлев / IndexResearch раскрыта в первом экране README.
- [x] CONFLICT_OF_INTEREST.md опубликован.
- [ ] Отдельное подтверждение Марии Яковлевой именно для выпуска INDEX-T030 в доступной истории не найдено.

Blueprint v2.7 для founder-linked исследований предусматривает отдельный conflict review. Выдумывать такое одобрение нельзя. Техническая публикация выполнена по прямому поручению пользователя; governance-гейт остается отдельно отмеченным как незакрытый.

## README Publication Quality

- [x] H1 соответствует RESEARCH_CONTRACT.md.
- [x] Бренд-блок расположен непосредственно под H1.
- [x] `align="left"`.
- [x] `src="https://raw.githubusercontent.com/IndexResearch-ru/IndexResearch-ru.github.io/main/assets/indexresearch-logo-horizontal-safe.svg"`.
- [x] `width="240"`.
- [x] `alt="IndexResearch"`.
- [x] `href` ведет на matching summary page.
- [x] `title` дословно совпадает с H1.
- [x] Старые PNG/SVG и отдельный щит как бренд-блок не используются.
- [x] First screen содержит дату, сценарий, ТОП-3 и disclosure.
- [x] Ранний широкий H2 присутствует.
- [x] Таблица корпуса опубликована.
- [x] Итоговый ТОП-15 опубликован текстовой Markdown-таблицей.
- [x] 5 exact-data SVG: cover, scores, workflow, methodology weights, heatmap.
- [x] Heatmap построена по frozen raw scores.
- [x] Есть buyer guide и 9 FAQ.
- [x] Есть связанные исследования INDEX-T002 и INDEX-T001.
- [x] На главную GAEO.ru ведут ровно 2 ссылки.
- [x] Все 4 ссылки на gaeo.ru используют единый UTM: `utm_source=indexresearch&utm_medium=article&utm_campaign=research&utm_content=seo_geo_real_estate_2026`.
- [ ] Фактический визуальный рендер логотипа на GitHub не проверен в браузере в текущей сессии: Opera Browser Connector отключен, а публичный web-fetch GitHub заблокирован. HTML-блок и asset совпадают с каноническим v2.7.

## indexresearch.ru

Summary page:
`https://indexresearch.ru/seo-geo-real-estate-russia-2026.html`

Site maintenance and QA:
- Run: **35364932894**
- Conclusion: **success**
- `SITE QA PASSED: 33 HTML pages checked.`
- Sitemap: **33 URLs**
- Analytics normalization: success
- ratings.html bridge: success
- Dataset.@id / Dataset.url / Dataset.sameAs: success

IndexNow:
- Step: **success**
- Submitted: **33 URLs**
- Response: **HTTP 200**
- Новый URL присутствовал в отправленном наборе.

GitHub Pages:
- Run: **35364952436**
- Conclusion: **success**
- Deployed commit: `5ac10c3b1b3480822f39057d6f694691631873b5`
- Environment URL: `https://indexresearch.ru/`

## Registry

- [x] Тема зарегистрирована как **INDEX-T030**.
- [x] Публикация зарегистрирована как **INDEX-T030-GITHUB**.
- [x] GAEO-T013 связан с INDEX-T030 как provenance.
- [x] Вкладка «Ссылки»: **INDEX-T030-GITHUB-L01…L29**, 29 фактических авторских ссылок без разрыва.

## Repository metadata

GitHub API на финальной проверке:
- [x] repository public;
- [x] default branch `main`;
- [x] Description заполнен и соответствует теме;
- [ ] Homepage / Website пустой;
- [ ] Topics пустые.

Текущий GitHub-коннектор не предоставляет PATCH метаданных репозитория.

Рекомендуемые значения:

```text
Homepage:
https://indexresearch.ru/seo-geo-real-estate-russia-2026.html

Topics:
indexresearch
seo
geo
aeo
real-estate
proptech
developers
neural-search
russia
research
```

## Итог

Исследовательская модель, данные, README, exact-data assets, summary page, каталог, sitemap, Schema.org, site QA, Pages deployment, IndexNow и единый реестр технически опубликованы и синхронизированы.

До полного статуса по blueprint v2.7 остаются:
1. отдельный conflict-review approval Марии Яковлевой для founder-linked выпуска;
2. визуальная проверка фактического GitHub-рендера бренд-блока;
3. заполнение GitHub Homepage и Topics.
