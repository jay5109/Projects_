
select CONVERT (DATE, order_date_DateOrders) as Date_of_order, 
        Product_name, 
        sum(Sales) as sum_sales, Order_Profit_Per_Order

from ProductData

-- Used INNER/LEFT JOIN to attach the fields/columns from MainTable to ProductData table using the same column, Category_Id
left join dbo.MainTable on dbo.ProductData.Category_Id = dbo.MainTable.Category_Id 

-- Used OUTER JOIN to  attach the fields/columns from OrderData to MainTable using the same column, Order_Id
full outer join dbo.OrderData on dbo.MainTable.Order_Id = dbo.OrderData.Order_Id

GROUP by Product_Name,order_date_DateOrders,Order_Profit_Per_Order

ORDER by order_date_DateOrders desc