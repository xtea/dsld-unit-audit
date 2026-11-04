# DSLD 审计:30 条分歧行标注

每条做两件事:照标签图在表格里填**印的数值、单位、%DV**,再在**类别**列写一个类别代码(见下表)。读者读数只供参考,以图为准。拿不准写在备注里。填完保存,告诉我「标完了」就行。请不要改每条标题里的编号(如 a13)和表格的列。

## 类别代码

| 代码 | 什么情况 | 怎么计 |
|---|---|---|
| DB_UNIT | 标签印的单位和库里不同(印 mcg,库存 mg) | 数据库错误 |
| DB_AMOUNT | 数字或小数点和库里不同 | 数据库错误 |
| DB_PCT | %DV 和库里不同 | 数据库错误 |
| LABEL_INCONSISTENT | 标签本身数值和 %DV 对不上,库照抄 | 标签错误 |
| OTHER_DV_BASIS | 标签自洽,%DV 按儿童/孕期/旧版 DV 算 | 检查误报 |
| COLUMN_OR_SERVING | 库取了另一栏或另一份量(每日量栏、儿童栏) | 单列报告 |
| IMAGE_MISMATCH | 图和记录不是同一产品或版本 | 单列报告 |
| CANNOT_DETERMINE | 看不清,或信息不够 | 不计入 |

## 常见情况

- 标签有多栏或多份量:找和库里份量对应的那一栏;库里取的是别的栏,写 COLUMN_OR_SERVING。
- %DV 印得很怪(比如 b340 的 333333%):照印的填,写 LABEL_INCONSISTENT。
- 图太小看不清:点每条的「DSLD 原页」看原始 PDF;还是看不清就写 CANNOT_DETERMINE。
- a18、b39、b117、b151、b199 这 5 条的多数票和之前放大看到的不一致,最需要你定。
- b340 你在核验页标过,已预填。
- 最后 3 条(附1–附3)是三个读者都判不了的,可选。附2、附3 三个读者读数一致,只是判定规则只认单位错;看着像数值录错(DB_AMOUNT),请确认。

## 30 条分歧行

### 1. a13 · Thiamine · 标签 61988

Trace Minerals Research — Power Pak Tangerine。标记类型:1000 倍(单位)。

**库里记录**:450 mg,30% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/61988)

![标签 61988](review30_imgs/a13_61988.jpg)

读者读数:Sonnet 450 mg, 30% · Opus 450 mg, 30% · Gemini 450 mcg, 30%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 450 | mg | 30 | LABEL_INCONSISTENT | 标签确实印 450 mg，非 mcg；与 30% 不相符。 |

---

### 2. a15 · Vitamin B6 · 标签 2883

Amazing Grass — Green SuperFood Chocolate。标记类型:1000 倍(单位)。

**库里记录**:38 mg,3% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/2883)

![标签 2883](review30_imgs/a15_2883.jpg)

读者读数:Sonnet 38 mg, 3% · Opus 38 mg, 3% · Gemini 0.38 mg, 3%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 38 | mg | 3 | LABEL_INCONSISTENT | 旋转放大后印的是 38 mg，未见小数点；与 3% 不相符。 |

---

### 3. a18 · Vitamin B12 · 标签 248129

Fresh Healthcare — Immune Support Multivitamin。标记类型:1000 倍(单位)。

**库里记录**:200 mg,8333% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/248129)

![标签 248129](review30_imgs/a18_248129.jpg)

读者读数:Sonnet 200 mcg, 8333% · Opus 200 mg, 8333% · Gemini 200 mcg, 8333%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 200 | mg | 8333 | LABEL_INCONSISTENT | 已核对原始 PDF；B12 印 200 mg，非 mcg。 |

---

### 4. b15 · Vitamin B2 · 标签 10248

Hi-Tech Pharmaceuticals — NitroPro Double Dutch Chocolate - Flavor。标记类型:1000 倍(单位)。

**库里记录**:850 mg,50% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/10248)

![标签 10248](review30_imgs/b15_10248.jpg)

读者读数:Sonnet 850 mcg, 50% · Opus 850 mg, 50% · Gemini 850 mg, 50%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 850 | mg | 50 | LABEL_INCONSISTENT | B2 行印 850 mg；邻行 B1 的 mcg 可清楚区分。 |

---

### 5. b33 · Pantothenic Acid · 标签 193269

Bodybuilding.com Foundation Series — Women's Multivitamin。标记类型:1000 倍(单位)。

**库里记录**:20 mcg,200% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/193269)

![标签 193269](review30_imgs/b33_193269.jpg)

读者读数:Sonnet 20 mg, 200% · Opus 20 mcg, 200% · Gemini 20 mcg, 200%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 20 | mcg | 200 | LABEL_INCONSISTENT | 标签泛酸行确实印 20 mcg。 |

---

### 6. b34 · Iodine · 标签 82168

New Sun — Advanced Thyroid Energy。标记类型:1000 倍(单位)。

**库里记录**:225 mg,150% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/82168)

![标签 82168](review30_imgs/b34_82168.jpg)

读者读数:Sonnet 225 mcg, 150% · Opus 225 mcg, 150% · Gemini 225 mg, 150%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 225 | mg | 150 | LABEL_INCONSISTENT | 碘行印 225 mg，非 mcg。 |

---

### 7. b39 · Vitamin E · 标签 303244

NeoLife — Prime Pack。标记类型:1000 倍(单位)。

**库里记录**:70 mcg,470% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/303244)

![标签 303244](review30_imgs/b39_303244.jpg)

读者读数:Sonnet 70 mcg, 470% · Opus 70 mg, 470% · Gemini 70 mg, 470%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 70 | mcg | 470 | LABEL_INCONSISTENT | 原始 PDF 印 70 mcg（105 IU）；单位与括号内 IU 及 470% 矛盾。 |

---

### 8. b57 · Vitamin E · 标签 269765

Core Nutritionals — GREENS Berry Bliss。标记类型:1000 倍(单位)。

**库里记录**:15 mcg,100% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/269765)

![标签 269765](review30_imgs/b57_269765.jpg)

读者读数:Sonnet 15 mg, 100% · Opus 15 mcg, 100% · Gemini 15 mcg, 100%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 15 | mcg | 100 | LABEL_INCONSISTENT | 维生素 E 行印 15 mcg，非 mg。 |

---

### 9. b103 · Pantothenic Acid · 标签 5126

Douglas Laboratories — Ultra Preventive Forte-Chel。标记类型:1000 倍(单位)。

**库里记录**:300 mcg,3000% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/5126)

![标签 5126](review30_imgs/b103_5126.jpg)

读者读数:Sonnet 300 mcg, 3000% · Opus 300 mcg, 3000% · Gemini 300 mg, 3000%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 300 | mcg | 3,000 | LABEL_INCONSISTENT | 泛酸行印 300 mcg；不按常识改成 mg。 |

---

### 10. b105 · Phosphorous · 标签 6975

Windmill — Milltrium Senior with Lutein & Lycopene。标记类型:1000 倍(单位)。

**库里记录**:20 mcg,2% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/6975)

![标签 6975](review30_imgs/b105_6975.jpg)

读者读数:Sonnet 20 mg, 2% · Opus 20 mcg, 2% · Gemini 20 mg, 2%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 20 | mcg | 2 | LABEL_INCONSISTENT | 旋转放大后磷行印 20 mcg，非 mg。 |

---

### 11. b117 · Biotin · 标签 247263

Salaam Nutritionals — Kid's Multivitamin。标记类型:1000 倍(单位)。

**库里记录**:60 mg,40% DV;适用人群:Children less than 4 years of age。[DSLD 原页](https://dsld.od.nih.gov/label/247263)

![标签 247263](review30_imgs/b117_247263.jpg)

读者读数:Sonnet 60 mcg, 20% · Opus 60 mg, 40% · Gemini 60 mg, 20%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 60 | mg | 40 | LABEL_INCONSISTENT | 标签印 60 mg；2–3 岁栏为 40%，4 岁及以上栏为 20%。库对应儿童栏，单位矛盾仍来自标签。 |

---

### 12. b143 · Vit. E · 标签 80196

Vibrant Health — Maximum Vibrance Chocolate Chunk。标记类型:1000 倍(单位)。

**库里记录**:120 mcg,800% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/80196)

![标签 80196](review30_imgs/b143_80196.jpg)

读者读数:Sonnet 120 mg, 800% · Opus 120 mcg, 800% · Gemini 120 mcg, 800%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 120 | mcg | 800 | LABEL_INCONSISTENT | 维生素 E 跨行印为 120 mcg/800%。 |

---

### 13. b148 · Vitamin B12 · 标签 331450

Chemical Free Body — Green 85。标记类型:1000 倍(单位)。

**库里记录**:2.6 mg,108% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/331450)

![标签 331450](review30_imgs/b148_331450.jpg)

读者读数:Sonnet 2.6 mcg, 108% · Opus 2.6 mg, 108% · Gemini 2.6 mg, 108%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 2.6 | mg | 108 | LABEL_INCONSISTENT | B12 行明确印 2.6 mg。 |

---

### 14. b149 · Molybdenum · 标签 27807

GNC Women's Ultra Mega — Maximum Nutrition Milk Chocolate。标记类型:1000 倍(单位)。

**库里记录**:75 mg,100% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/27807)

![标签 27807](review30_imgs/b149_27807.jpg)

读者读数:Sonnet 75 mcg, 100%(看不清) · Opus 75 mcg, 100%(看不清) · Gemini 75 mcg, 100%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 75 | mg | 100 | LABEL_INCONSISTENT | 原始 PDF 放大后钼行印 75 mg，与 100% 不相符。 |

---

### 15. b151 · Iron · 标签 252266

Nugevity — MM6 For Women。标记类型:1000 倍(单位)。

**库里记录**:9 mcg,50% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/252266)

![标签 252266](review30_imgs/b151_252266.jpg)

读者读数:Sonnet 9 mg, 50% · Opus 9 mcg, 50% · Gemini 9 mg, 50%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 9 | mcg | 50 | LABEL_INCONSISTENT | 铁行印 9 mcg，非 mg。 |

---

### 16. b173 · Vitamin K1 · 标签 304382

G6 Sports — Super-Lean Deluxe Meal Replacement Peanut Butter Milkshake。标记类型:1000 倍(单位)。

**库里记录**:10 mg,13.2% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/304382)

![标签 304382](review30_imgs/b173_304382.jpg)

读者读数:Sonnet 10 mg, 13.2% · Opus 10 mcg, 13.2% · Gemini 10 mcg, 13.2%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 10 | mcg | 13.2 | DB_UNIT | K1 行印 10 mcg，库录为 mg；%DV 照印刷值保留。 |

---

### 17. b199 · Molybdenum · 标签 3216

Trace Minerals Research — Super Mineral Juice Peach Pizzaz。标记类型:1000 倍(单位)。

**库里记录**:100 mg,135% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/3216)

![标签 3216](review30_imgs/b199_3216.jpg)

读者读数:Sonnet 100 mcg, 135% · Opus 100 mg, 135% · Gemini 100 mg, 135%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 100 | mg | 135 | LABEL_INCONSISTENT | 钼行印 100 mg；上下碘、硒行的 mcg 可区分。 |

---

### 18. b206 · Vitamin E · 标签 309215

GliSODin Skin Nutrients — Advanced Skin Brightening Formula。标记类型:1000 倍(单位)。

**库里记录**:33.5 mcg,223% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/309215)

![标签 309215](review30_imgs/b206_309215.jpg)

读者读数:Sonnet 33.5 mg, 223% · Opus 33.5 mg, 223% · Gemini 33.5 mcg, 223%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 33.5 | mcg | 223 | LABEL_INCONSISTENT | 英文 Supplement Facts 的维生素 E 行印 33.5 mcg。 |

---

### 19. b215 · Choline · 标签 244513

Mason Natural — Body, Hair, Skin, & Nails Strawberry Coconut Flavors。标记类型:1000 倍(单位)。

**库里记录**:40 mcg,8% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/244513)

![标签 244513](review30_imgs/b215_244513.jpg)

读者读数:Sonnet 40 mg, 8% · Opus 40 mcg, 8% · Gemini 40 mcg, 8%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 40 | mcg | 8 | LABEL_INCONSISTENT | 胆碱行印 40 mcg，非 mg。 |

---

### 20. b234 · Vitamin B12 · 标签 278697

ZIKS Nnodum Pharmaceuticals — Prenatal Vitamins Plus。标记类型:1000 倍(单位)。

**库里记录**:12 mg,429% DV;适用人群:Pregnant and Lactating。[DSLD 原页](https://dsld.od.nih.gov/label/278697)

![标签 278697](review30_imgs/b234_278697.jpg)

读者读数:Sonnet ? ?, —%(看不清) · Opus ? ?, —%(看不清) · Gemini 12 mcg, 429%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 12 | mcg | 429 | DB_UNIT | 原始 PDF 旋转放大确认 12 mcg；库录为 mg。标签注明孕期及哺乳期 DV。 |

---

### 21. b237 · Thiamine · 标签 2489

Amazing Grass — Green SuperFood Raw Reserve。标记类型:1000 倍(单位)。

**库里记录**:0.4 mcg,25% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/2489)

![标签 2489](review30_imgs/b237_2489.jpg)

读者读数:Sonnet 0.4 mg, 25% · Opus 0.4 mcg, 25% · Gemini 0.4 mcg, 25%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 0.4 | mcg | 25 | LABEL_INCONSISTENT | 硫胺素行印 0.4 mcg，非 mg。 |

---

### 22. b251 · Magnesium · 标签 298502

NaturesPlus Source of Life Animal Parade — MagKidz Cherry。标记类型:10 倍。

**库里记录**:100 mg,125% DV;适用人群:Children less than 4 years of age。[DSLD 原页](https://dsld.od.nih.gov/label/298502)

![标签 298502](review30_imgs/b251_298502.jpg)

读者读数:Sonnet 100 mg, 125% · Opus 100 mg, 125% · Gemini 100 mg, 24%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 100 | mg | 125 | OTHER_DV_BASIS | 1–3 岁栏为 125%，成人及 ≥4 岁栏为 24%；库对应儿童栏。 |

---

### 23. b259 · Vitamin B12 · 标签 181149

NuMedica — Multiplex Complete Wild Berry Flavor。标记类型:10 倍。

**库里记录**:200 mcg,333% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/181149)

![标签 181149](review30_imgs/b259_181149.jpg)

读者读数:Sonnet 200 mcg, 333% · Opus 200 mcg, 333% · Gemini 200 mcg, 3333%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 200 | mcg | 333 | LABEL_INCONSISTENT | B12 行只印 333%，非 3333%；库照抄标签。 |

---

### 24. b279 · Copper · 标签 205673

Green Label — Premium Prenatal Multivitamin。标记类型:10 倍。

**库里记录**:13.2 mg,100% DV;适用人群:Pregnant and Lactating。[DSLD 原页](https://dsld.od.nih.gov/label/205673)

![标签 205673](review30_imgs/b279_205673.jpg)

读者读数:Sonnet 2 mg, 100%(看不清) · Opus 2 mg, 100%(看不清) · Gemini 2 mg, 100%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 13%2 | mg | 100 | CANNOT_DETERMINE | 原始 PDF 的数值位置可见异常字串“13%2 mg”；不能可靠解释成 13.2 或 2，不强行纠正。 |

---

### 25. b295 · Magnesium · 标签 270337

Espira by Avon — Kids Multivitamins Very Berry。标记类型:10 倍。

**库里记录**:5.5 mg,20% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/270337)

![标签 270337](review30_imgs/b295_270337.jpg)

读者读数:Sonnet 83 mg, 20%(看不清) · Opus 83 mg, 20%(看不清) · Gemini 85 mg, 20%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| ? | mg | 20 | CANNOT_DETERMINE | 已放大原始 PDF；镁数值疑似 83（也可能 85），低清晰度下不能可靠确定，不用 %DV 反推。 |

---

### 26. b302 · Magnesium · 标签 204730

Bluebonnet Rainforest Animalz  — Multiple Cherry Flavor。标记类型:10 倍。

**库里记录**:10 mg,13% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/204730)

![标签 204730](review30_imgs/b302_204730.jpg)

读者读数:Sonnet 10 mg, 2% · Opus 10 mg, 13% · Gemini 10 mg, 13%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 10 | mg | 2 | COLUMN_OR_SERVING | 对应库中 ≥4 岁人群的右栏印 2%；13% 是左侧 <4 岁儿童栏。 |

---

### 27. b316 · Magnesium · 标签 239971

XYMOGEN — ActivNutrients Chewable Natural Mixed Berry Flavor。标记类型:10 倍。

**库里记录**:50 mg,63% DV;适用人群:Children less than 4 years of age。[DSLD 原页](https://dsld.od.nih.gov/label/239971)

![标签 239971](review30_imgs/b316_239971.jpg)

读者读数:Sonnet 50 mg, 63% · Opus 50 mg, 12% · Gemini 50 mg, 63%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 50 | mg | 63 | OTHER_DV_BASIS | 1–3 岁栏为 63%，成人及 ≥4 岁栏为 12%；库对应儿童栏。 |

---

### 28. b328 · Riboflavin · 标签 256009

Life's Fortune — Life's Energy。标记类型:10 倍。

**库里记录**:5 mg,2059% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/256009)

![标签 256009](review30_imgs/b328_256009.jpg)

读者读数:Sonnet 5 MG, 2059% · Opus 5 MG, 2059% · Gemini 35 MG, 2059%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 5 | MG | 2059 | LABEL_INCONSISTENT | 核黄素行印 5 MG，非 35 MG；与 2059% 不相符。 |

---

### 29. b337 · Vitamin B6 · 标签 251829

AN Amazing Nutrition Amazing Formulas — Digestive Support。标记类型:10 倍。

**库里记录**:20 mg,100% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/251829)

![标签 251829](review30_imgs/b337_251829.jpg)

读者读数:Sonnet 20 mg, —%(看不清) · Opus 20 mg, —% · Gemini 20 mg, 1000%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 20 | mg | ? | CANNOT_DETERMINE | 原始 PDF 右缘弯曲且模糊，B6 的 %DV 无法可靠区分 100 与 1000。 |

---

### 30. b340 · Biotin · 标签 223197

Vital Nutrients — Biotin 10 mg。标记类型:10 倍。

**库里记录**:10 mg,333333% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/223197)

![标签 223197](review30_imgs/b340_223197.jpg)

读者读数:Sonnet 10 mg, 33.3333% · Opus 10 mg, 333333% · Gemini 10 mg, 333333%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| 10 | mg | 33,3333 | LABEL_INCONSISTENT | 核验页已标；标签原样印“33,3333%”（逗号位置异常），去掉逗号为库中的 333333。 |

---

## 可选:三个读者都判不了的 3 条

### 附1. b65 · Molybdenum · 标签 19982

Ultima — Ultima Replenisher Grape。标记类型:1000 倍(单位)。

**库里记录**:3.5 mg,5% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/19982)

![标签 19982](review30_imgs/b65_19982.jpg)

读者读数:Sonnet 4.5 mcg, 6%(看不清) · Opus ? mcg, 6%(看不清) · Gemini ? ?, —%(看不清)

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| | | |  | |

---

### 附2. b83 · Vitamin B12 · 标签 69299

Natures Plus — UIltra Skinny Mini。标记类型:1000 倍(单位)。

**库里记录**:1000 mcg,16.667% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/69299)

![标签 69299](review30_imgs/b83_69299.jpg)

读者读数:Sonnet 500 mcg, 8333% · Opus 500 mcg, 8333% · Gemini 500 mcg, 8333%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| | | |  | |

---

### 附3. b100 · Vitamin A · 标签 2054

Gaspari Nutrition — Gaspari's MyoFusion Delicious Vanilla。标记类型:1000 倍(单位)。

**库里记录**:1.25 IU,25% DV;适用人群:Adults and children 4 or more years of age。[DSLD 原页](https://dsld.od.nih.gov/label/2054)

![标签 2054](review30_imgs/b100_2054.jpg)

读者读数:Sonnet 1250 IU, 25% · Opus 1250 IU, 25% · Gemini 1250 IU, 25%

| 印的数值 | 印的单位 | 印的 %DV | 类别 | 备注 |
|---|---|---|---|---|
| | | |  | |

---
