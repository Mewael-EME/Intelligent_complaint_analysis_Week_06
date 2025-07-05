### 🔍 Task 1: Exploratory Data Analysis (EDA) Summary

The original dataset contained approximately **1,048,575 records**. After filtering to include only complaints related to the five targeted product categories — *Credit card, Personal loan, Buy Now Pay Later (BNPL), Savings account, and Money transfers* — **17,512 rows** remained.

Next, we removed complaints with missing narratives, resulting in a final working dataset of **5,018 complaints with valid narrative text**. This means over **71%** of the initially filtered complaints lacked usable narrative content.

The cleaned narratives vary significantly in length, ranging from as short as **6 words** to over **5,264 words**, with an average word count of approximately **213 words per complaint**. This variability in text length highlights the importance of implementing a chunking strategy in the next stage to ensure consistent embedding and retrieval performance.
 
