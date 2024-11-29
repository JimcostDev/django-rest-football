SELECT pg_get_serial_sequence('public.team_team', 'id');
SELECT MAX(id) + 1 AS next_id FROM public.team_team; -- retorna 45
ALTER SEQUENCE public.team_team_id_seq RESTART WITH 45; -- altero la secuencia al dicho valor