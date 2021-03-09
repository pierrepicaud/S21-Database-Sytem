CREATE FUNCTION get_address1()
returns table( address VARCHAR(45))
as
$$
begin
return query
select address.address from address
where
	('11' LIKE '%' || address.address || '%') AND
	(address.city_id BETWEEN 400 AND 600)
;
end;
$$
language plpgsql;
