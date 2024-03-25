-- 코드를 작성해주세요
SELECT A.ITEM_ID,A.ITEM_NAME,A.RARITY FROM ITEM_INFO A
JOIN ITEM_TREE B ON A.ITEM_ID = B.ITEM_ID
WHERE A.ITEM_ID NOT IN (SELECT PARENT_ITEM_ID FROM ITEM_TREE WHERE PARENT_ITEM_ID IS NOT NULL)
ORDER BY A.ITEM_ID DESC