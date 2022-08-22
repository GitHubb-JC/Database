-- 1. ----------------------------------------
select *
from playlist_track
order by playlistId desc
limit 5;

-- 2. -----------------------------------------
select *
from tracks
order by TrackId
limit 5;

-- 3. --------------------------
select playlist_track.playlistid, tracks.Name
from tracks inner join playlist_track
    on tracks.TrackId = playlist_track.TrackId
order by Name desc
limit 5;

-- 4. -------------------------------
select playlist_track.PlaylistId, tracks.Name
from playlist_track inner join tracks
    on playlist_track.TrackId = tracks.TrackId
where playlist_track.PlaylistId = 10
order by Name DESC
limit 5;

-- 5. -------------------------------
select count(*)
from tracks inner join artists
    on tracks.Composer = artists.Name;

-- 6. -------------------------------
select count(*)
from tracks left join artists
    on tracks.Composer = artists.Name;

-- 8. ---------------------------------
select InvoiceLineId, InvoiceId
from invoice_items
order by InvoiceId
limit 5;

-- 9. -----------------------------------------
select InvoiceId, CustomerId
from invoices
order by InvoiceId
limit 5;

-- 10. ---------------------------------------
select invoice_items.InvoiceLineId, invoices.InvoiceId
from invoice_items left join invoices
    on invoice_items.InvoiceId = invoices.InvoiceId
order by invoice_items.InvoiceId desc
limit 5;

-- 11. -----------------------------------------
select invoices.invoiceid, customers.CustomerId
from invoices left join customers
    on invoices.customerId = customers.CustomerId
order by invoices.InvoiceId DESC
limit 5;

-- 12. ------------------------------------------------
select 
    invoice_items.InvoiceLineId,
    invoices.InvoiceId,
    customers.CustomerId
from invoice_items 
    left join invoices
        on invoice_items.InvoiceId = invoices.InvoiceId
    left join customers
        on invoices.CustomerId = customers.CustomerId
order by invoices.InvoiceId DESC
limit 5;

-- 13. ----------------------------------------------
select customers.CustomerId, count(*)
from customers 
    left join invoices
        on customers.CustomerId = invoices.CustomerId
    left join invoice_items
        on invoices.InvoiceId = invoice_items.InvoiceId
group by customers.CustomerId
order by customers.CustomerId
LIMIT 5;

select customers.CustomerId, invoices.invoiceId
from customers 
    left join invoices
        on customers.CustomerId = invoices.CustomerId
where invoices.invoiceId = 99
group by customers.CustomerId
order by customers.CustomerId
limit 5;