DROP MATERIALIZED VIEW IF EXISTS sentient.customer_by_tenant_and_title;

CREATE MATERIALIZED VIEW IF NOT EXISTS sentient.customer_by_tenant_and_title AS
    SELECT *
    from sentient.customer
    WHERE tenant_id IS NOT NULL AND title IS NOT NULL AND id IS NOT NULL
    PRIMARY KEY ( tenant_id, title, id )
    WITH CLUSTERING ORDER BY ( title ASC, id DESC );
