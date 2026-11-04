# DSLD 审计:随机 30 条抽查

这 30 条是从「三个模型读数完全一致」的行里随机抽的(种子 20261104)。为避免先入为主,这次不显示模型的读数。做法和上次一样:照标签图填**印的数值、单位、%DV**,在**类别**列写代码,拿不准写备注。填完说「标完了」。不要改标题编号和表格的列。

类别代码:`DB_UNIT`(单位和库不同)· `DB_AMOUNT`(数字不同)· `DB_PCT`(%DV 不同)· `LABEL_INCONSISTENT`(和库一样,标签本身矛盾)· `OTHER_DV_BASIS`(%DV 按儿童/孕期/旧版 DV)· `COLUMN_OR_SERVING`(库取了别的栏或份量)· `IMAGE_MISMATCH`(图和记录不是同一产品)· `CANNOT_DETERMINE`(看不清)

---

### 1. b219 · Selenium · 标签 261150

MN Morphogen Nutrition — Macrogen Homemade Apple Pie。

**库里记录**:17.5 mg,25% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/261150)

![标签 261150](spot30_imgs/b219_261150.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 17.5 | ml | 25 | DB_UNIT | 已核对原始 PDF，硒行印“17.5ml”；标签单位本身异常，既不是库中的 mg，也不能擅自补成 mcg。 |

---

### 2. b179 · Vitamin A · 标签 284995

Puritan's Pride — Cod Liver Oil。

**库里记录**:375 mg,42% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/284995)

![标签 284995](spot30_imgs/b179_284995.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 375 | mcg | 42 | DB_UNIT | Vitamin A 行印 375 mcg；库录为 mg。 |

---

### 3. b22 · Selenium · 标签 264259

Medecor Pharma — TriCare Prenatal Chewable Tablets。

**库里记录**:32.5 mg,46.5% DV;适用人群:Pregnant and Lactating。[DSLD 原页](https://dsld.od.nih.gov/label/264259)

![标签 264259](spot30_imgs/b22_264259.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 32.5 | mcg | 46.5 | DB_UNIT | Selenium 行印 32.5 mcg；库录为 mg。 |

---

### 4. b66 · Potassium · 标签 206778

PureFormulas — PureMulti for Men。

**库里记录**:99 mcg,2% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/206778)

![标签 206778](spot30_imgs/b66_206778.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 99 | mg | 2 | DB_UNIT | 旋转放大后 Potassium 行印 99 mg；库录为 mcg。 |

---

### 5. b79 · Thiamine · 标签 3280

Highland Laboratories — Women's 30 Plus Multi。

**库里记录**:30 mcg,2000% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/3280)

![标签 3280](spot30_imgs/b79_3280.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 30 | mg | 2,000 | DB_UNIT | Thiamin 行印 30 mg；库录为 mcg。 |

---

### 6. b126 · Riboflavin · 标签 288129

Rainbow Light — Active Health Teen Multivitamin。

**库里记录**:30 mcg,2308% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/288129)

![标签 288129](spot30_imgs/b126_288129.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 30 | mg | 2308 | DB_UNIT | Riboflavin（vitamin B2）行印 30 mg；库录为 mcg。 |

---

### 7. b162 · Folic Acid · 标签 273629

OLLY — Lil'Ollys Kids' Multi + Probiotic Yum Berry Punch。

**库里记录**:200 mg,50% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/273629)

![标签 273629](spot30_imgs/b162_273629.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 200 | mcg | 50 | DB_UNIT | 按 ≥4 岁、2 颗软糖右栏填写；2–3 岁、1 颗左栏为 100 mcg、50%。库对应右栏但单位录为 mg。 |

---

### 8. a9 · Vitamin A · 标签 304930

GSK — Centrum Silver Men 50+。

**库里记录**:1050 mg,117% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/304930)

![标签 304930](spot30_imgs/a9_304930.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 1050 | mcg | 117 | DB_UNIT | Vitamin A 行印 1050 mcg；库录为 mg。 |

---

### 9. b36 · Biotin · 标签 265728

Carlson — Moistur-Eyes。

**库里记录**:300 mg,1000% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/265728)

![标签 265728](spot30_imgs/b36_265728.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 300 | mcg | 1,000 | DB_UNIT | Biotin 行印 300 mcg；库录为 mg。 |

---

### 10. b88 · Manganese · 标签 40833

Higher Nature — True Food Supernutrition Plus。

**库里记录**:0.67 mcg,34% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/40833)

![标签 40833](spot30_imgs/b88_40833.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 0.67 | mg | 34 | DB_UNIT | 每片 Manganese 印 0.67 mg；库录为 mcg。百分比表头为 %RDA，脚注注明 new 2009 values。 |

---

### 11. a2 · Vitamin K-2 · 标签 262352

Wonder Laboratories — Ipriflavone。

**库里记录**:60 mg,50% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/262352)

![标签 262352](spot30_imgs/a2_262352.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 60 | mcg | 50 | DB_UNIT | Vitamin K-2 行印 60 mcg；库录为 mg。 |

---

### 12. b188 · Vitamin B6 · 标签 333849

PMD — Amplify XL Vanilla Flex。

**库里记录**:0.2 mcg,12% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/333849)

![标签 333849](spot30_imgs/b188_333849.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 0.2 | mg | 12 | DB_UNIT | 放大后 Vitamin B6 行印 0.2 mg；库录为 mcg。 |

---

### 13. b141 · Vitamin B12 · 标签 36676

Thompson — B12 Lozenge 1000 mg Natural Cherry Flavor。

**库里记录**:1000 mg,16667% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/36676)

![标签 36676](spot30_imgs/b141_36676.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 1000 | mcg | 16,667 | DB_UNIT | 正面和成分表均印 1000 mcg；成人及 ≥4 岁栏为 16,667%，孕期哺乳期栏为 12,500%。 |

---

### 14. b161 · Vitamin D3 · 标签 252786

BulkSupplements.com — Vitamin D3。

**库里记录**:125 mg,625% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/252786)

![标签 252786](spot30_imgs/b161_252786.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 125 | mcg | 625 | DB_UNIT | D3 行印 125 mcg；50 milligrams 是产品每份重量，不是 D3 含量。 |

---

### 15. b175 · Vitamin B6 · 标签 49294

Nature's Plus — Mega-Stress Complex。

**库里记录**:100 mcg,5000% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/49294)

![标签 49294](spot30_imgs/b175_49294.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 100 | mg | 5000 | DB_UNIT | Vitamin B6 行印 100 mg；库录为 mcg。 |

---

### 16. b202 · Chromium · 标签 18989

Equate — Complete Multivitamin。

**库里记录**:35 mg,29% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/18989)

![标签 18989](spot30_imgs/b202_18989.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 35 | mcg | 29 | DB_UNIT | Chromium 行印 35 mcg；库录为 mg。 |

---

### 17. a27 · Molybdenum · 标签 255683

Solaray — Thyroid Caps。

**库里记录**:50 mg,67% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/255683)

![标签 255683](spot30_imgs/a27_255683.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 50 | mcg | 67 | DB_UNIT | Molybdenum 行印 50 mcg；库录为 mg。 |

---

### 18. b115 · Vitamin D · 标签 212200

Sundown Kids — Complete Multivitamin Gummies Cars。

**库里记录**:7.5 mg,50% DV;适用人群:Children less than 4 years of age。[DSLD 原页](https://dsld.od.nih.gov/label/212200)

![标签 212200](spot30_imgs/b115_212200.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 7.5 | mcg | 50 | DB_UNIT | 按 2–3 岁、1 颗软糖栏填写，印 7.5 mcg（300 IU）、50%；≥4 岁、2 颗栏为 15 mcg（600 IU）、75%。 |

---

### 19. b82 · Biotin · 标签 328204

Blueprint Bryan Johnson — Essential Capsules。

**库里记录**:50 mg,167% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/328204)

![标签 328204](spot30_imgs/b82_328204.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 50 | mcg | 167 | DB_UNIT | Biotin 行印 50 mcg；库录为 mg。 |

---

### 20. a11 · Vitamin B12 · 标签 251385

AN Amazing Nutrition Amazing Formulas — Women's One Multiple。

**库里记录**:25 mg,417% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/251385)

![标签 251385](spot30_imgs/a11_251385.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 25 | mcg | 417 | DB_UNIT | Vit B-12 行印 25 mcg；库录为 mg。 |

---

### 21. b111 · Folic Acid · 标签 4328

Nature's Bounty — Your Life Multi Men's 45+。

**库里记录**:400 mg,100% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/4328)

![标签 4328](spot30_imgs/b111_4328.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 400 | mcg | 100 | DB_UNIT | Folic Acid 行印 400 mcg；库录为 mg。 |

---

### 22. b198 · Niacin · 标签 42566

Creative Bioscience — hCG 1234。

**库里记录**:0.475 mcg,2% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/42566)

![标签 42566](spot30_imgs/b198_42566.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| .475 | mg | 2 | DB_UNIT | Niacin 原样印“.475 mg”；与 0.475 数值相同，库单位录为 mcg。 |

---

### 23. b8 · Manganese · 标签 316413

Bluebonnet — Multi One。

**库里记录**:5 mcg,217% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/316413)

![标签 316413](spot30_imgs/b8_316413.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 5 | mg | 217 | DB_UNIT | Manganese 行印 5 mg；库录为 mcg。 |

---

### 24. b144 · Vitamin D3 · 标签 248355

NutraBio — First Response Citrus Orange。

**库里记录**:50 mg,250% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/248355)

![标签 248355](spot30_imgs/b144_248355.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 50 | mcg | 250 | DB_UNIT | Vitamin D3 行印 50 mcg（2,000 IU）；库录为 mg。 |

---

### 25. b119 · Vitamin B6 · 标签 277605

Researched Nutritionals — Physician's Daily Multivitamin + D3。

**库里记录**:5 mcg,294% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/277605)

![标签 277605](spot30_imgs/b119_277605.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 5 | mg | 294 | DB_UNIT | Vitamin B6 行印 5 mg；库录为 mcg。 |

---

### 26. b205 · Calcium · 标签 178368

Bluebonnet — Calcium Citrate Magnesium Vitamin D3。

**库里记录**:1000 mcg,77% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/178368)

![标签 178368](spot30_imgs/b205_178368.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 1000 | mg | 77 | DB_UNIT | Calcium 行印 1000 mg；库录为 mcg。 |

---

### 27. b40 · Manganese · 标签 237144

Viva Vitamins — Complete Minerals Regular Strength Iron & Copper Free。

**库里记录**:1 mcg,43% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/237144)

![标签 237144](spot30_imgs/b40_237144.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 1 | mg | 43 | DB_UNIT | Manganese 行印 1 mg；库录为 mcg。 |

---

### 28. a43 · Magnesium · 标签 246585

Nutracraft — SugarPro。

**库里记录**:125 mcg,31% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/246585)

![标签 246585](spot30_imgs/a43_246585.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 125 | mg | 31 | DB_UNIT | 放大后 Magnesium 行印 125 mg；库录为 mcg。 |

---

### 29. b55 · Potassium · 标签 262188

MRM Nutrition — Egg White Protein Chocolate Flavored。

**库里记录**:410 mcg,8% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/262188)

![标签 262188](spot30_imgs/b55_262188.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 410 | mg | 8 | DB_UNIT | Nutrition Facts 底部 Potassium 行印 410 mg、8%；库录为 mcg。 |

---

### 30. b201 · Vitamin C · 标签 210576

GNC AMP Advanced Muscle Performance — Mega Men Sport Multivitamin。

**库里记录**:300 mcg,333% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/210576)

![标签 210576](spot30_imgs/b201_210576.jpg)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 300 | mg | 333 | DB_UNIT | 图为组合装；对应的 Mega Men Sport Multivitamin 成分表中 Vitamin C 印 300 mg，份量为 2 片。 |

---
