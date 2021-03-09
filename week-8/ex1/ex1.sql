CREATE FUNCTION get_address1();
returns table( address VARCHAR(45))
as
$$
begin
return query
SELECT address.address FROM address
WHERE address.address LIKE '%11%'
AND address.city_id BETWEEN 400 AND 600
;
end;
$$
language plpgsql;
