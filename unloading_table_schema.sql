DO $$
DECLARE
    t_name varchar;
    row_now json;
    json_file json = NULL;
BEGIN
    FOR t_name IN
        select table_name from information_schema.tables where table_schema = 'main'
        LOOP
            row_now = json_build_object(
                t_name, (FORMAT('{%s}'::text, (
                    select string_agg(FORMAT('"%s": "%s"', column_name, data_type)::varchar, ', ')
                    from information_schema.columns
                    where table_name = t_name
                      )
                  )
                )::jsonb
              );
            IF json_file IS NULL THEN
                json_file = row_now::jsonb;
            ELSE
                json_file = json_file::jsonb || row_now::jsonb;
            END IF;
        END LOOP;
    raise notice '%', json_file;
END;
$$;
unloading_table_schema
