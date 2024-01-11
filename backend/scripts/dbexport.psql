--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4
-- Dumped by pg_dump version 15.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: app; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA app;


ALTER SCHEMA app OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: games; Type: TABLE; Schema: app; Owner: okcapplicant
--

CREATE TABLE app.games (
    id integer NOT NULL,
    date date NOT NULL,
    home_team_id integer,
    away_team_id integer
);


ALTER TABLE app.games OWNER TO okcapplicant;

--
-- Name: games_id_seq; Type: SEQUENCE; Schema: app; Owner: okcapplicant
--

CREATE SEQUENCE app.games_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE app.games_id_seq OWNER TO okcapplicant;

--
-- Name: games_id_seq; Type: SEQUENCE OWNED BY; Schema: app; Owner: okcapplicant
--

ALTER SEQUENCE app.games_id_seq OWNED BY app.games.id;


--
-- Name: players; Type: TABLE; Schema: app; Owner: okcapplicant
--

CREATE TABLE app.players (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE app.players OWNER TO okcapplicant;

--
-- Name: players_id_seq; Type: SEQUENCE; Schema: app; Owner: okcapplicant
--

CREATE SEQUENCE app.players_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE app.players_id_seq OWNER TO okcapplicant;

--
-- Name: players_id_seq; Type: SEQUENCE OWNED BY; Schema: app; Owner: okcapplicant
--

ALTER SEQUENCE app.players_id_seq OWNED BY app.players.id;


--
-- Name: playerstats; Type: TABLE; Schema: app; Owner: okcapplicant
--

CREATE TABLE app.playerstats (
    id integer NOT NULL,
    game_id integer,
    player_id integer,
    is_starter boolean NOT NULL,
    minutes integer,
    points integer,
    assists integer,
    offensive_rebounds integer,
    defensive_rebounds integer,
    steals integer,
    blocks integer,
    turnovers integer,
    defensive_fouls integer,
    offensive_fouls integer,
    free_throws_made integer,
    free_throws_attempted integer,
    two_pointers_made integer,
    two_pointers_attempted integer,
    three_pointers_made integer,
    three_pointers_attempted integer
);


ALTER TABLE app.playerstats OWNER TO okcapplicant;

--
-- Name: playerstats_id_seq; Type: SEQUENCE; Schema: app; Owner: okcapplicant
--

CREATE SEQUENCE app.playerstats_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE app.playerstats_id_seq OWNER TO okcapplicant;

--
-- Name: playerstats_id_seq; Type: SEQUENCE OWNED BY; Schema: app; Owner: okcapplicant
--

ALTER SEQUENCE app.playerstats_id_seq OWNED BY app.playerstats.id;


--
-- Name: shotdata; Type: TABLE; Schema: app; Owner: okcapplicant
--

CREATE TABLE app.shotdata (
    id integer NOT NULL,
    player_stats_id integer,
    is_make boolean NOT NULL,
    location_x numeric,
    location_y numeric
);


ALTER TABLE app.shotdata OWNER TO okcapplicant;

--
-- Name: shotdata_id_seq; Type: SEQUENCE; Schema: app; Owner: okcapplicant
--

CREATE SEQUENCE app.shotdata_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE app.shotdata_id_seq OWNER TO okcapplicant;

--
-- Name: shotdata_id_seq; Type: SEQUENCE OWNED BY; Schema: app; Owner: okcapplicant
--

ALTER SEQUENCE app.shotdata_id_seq OWNED BY app.shotdata.id;


--
-- Name: teams; Type: TABLE; Schema: app; Owner: okcapplicant
--

CREATE TABLE app.teams (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE app.teams OWNER TO okcapplicant;

--
-- Name: teams_id_seq; Type: SEQUENCE; Schema: app; Owner: okcapplicant
--

CREATE SEQUENCE app.teams_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE app.teams_id_seq OWNER TO okcapplicant;

--
-- Name: teams_id_seq; Type: SEQUENCE OWNED BY; Schema: app; Owner: okcapplicant
--

ALTER SEQUENCE app.teams_id_seq OWNED BY app.teams.id;


--
-- Name: games id; Type: DEFAULT; Schema: app; Owner: okcapplicant
--

ALTER TABLE ONLY app.games ALTER COLUMN id SET DEFAULT nextval('app.games_id_seq'::regclass);


--
-- Name: players id; Type: DEFAULT; Schema: app; Owner: okcapplicant
--

ALTER TABLE ONLY app.players ALTER COLUMN id SET DEFAULT nextval('app.players_id_seq'::regclass);


--
-- Name: playerstats id; Type: DEFAULT; Schema: app; Owner: okcapplicant
--

ALTER TABLE ONLY app.playerstats ALTER COLUMN id SET DEFAULT nextval('app.playerstats_id_seq'::regclass);


--
-- Name: shotdata id; Type: DEFAULT; Schema: app; Owner: okcapplicant
--

ALTER TABLE ONLY app.shotdata ALTER COLUMN id SET DEFAULT nextval('app.shotdata_id_seq'::regclass);


--
-- Name: teams id; Type: DEFAULT; Schema: app; Owner: okcapplicant
--

ALTER TABLE ONLY app.teams ALTER COLUMN id SET DEFAULT nextval('app.teams_id_seq'::regclass);


--
-- Data for Name: games; Type: TABLE DATA; Schema: app; Owner: okcapplicant
--

COPY app.games (id, date, home_team_id, away_team_id) FROM stdin;
1	2022-12-19	1	2
2	2022-12-21	1	2
3	2023-02-10	2	1
4	2023-03-26	2	1
\.


--
-- Data for Name: players; Type: TABLE DATA; Schema: app; Owner: okcapplicant
--

COPY app.players (id, name) FROM stdin;
1	Michael Jordan
2	Tweety
3	Bugs Bunny
4	Daffy Duck
5	Sniffles
6	Yosemite Sam
7	Road Runner
8	Porky Pig
9	Sylvester
10	Lola Bunny
11	Wile E. Coyote
12	Bill Murray
13	Barnyard Dawg
14	Tasmanian Devil
15	Foghorn Leghorn
16	Elmer Fudd
17	Monstar 1
18	Monstar 2
19	Monstar 3
20	Monstar 4
21	Monstar 5
22	Monstar 6
23	Monstar 7
24	Monstar 8
25	Monstar 9
26	Monstar 10
27	Monstar 11
28	Monstar 12
29	Monstar 13
30	Monstar 14
31	Monstar 15
\.


--
-- Data for Name: playerstats; Type: TABLE DATA; Schema: app; Owner: okcapplicant
--

COPY app.playerstats (id, game_id, player_id, is_starter, minutes, points, assists, offensive_rebounds, defensive_rebounds, steals, blocks, turnovers, defensive_fouls, offensive_fouls, free_throws_made, free_throws_attempted, two_pointers_made, two_pointers_attempted, three_pointers_made, three_pointers_attempted) FROM stdin;
1	1	17	f	16	12	1	0	3	0	1	0	1	0	0	0	0	0	4	5
2	1	18	t	35	35	6	0	2	1	2	2	2	0	14	14	9	23	1	1
3	1	19	f	28	12	2	1	3	2	0	2	2	1	0	0	3	4	2	3
4	1	20	t	31	13	0	2	1	1	0	2	4	1	7	8	3	6	0	2
5	1	21	t	23	8	3	3	3	0	1	2	2	0	2	4	3	5	0	4
6	1	22	f	23	11	1	0	3	1	0	0	1	0	0	0	1	1	3	6
7	1	23	f	10	1	1	0	1	0	0	0	1	0	1	1	0	0	0	3
8	1	27	t	25	12	1	2	2	1	0	0	2	0	4	4	4	6	0	3
9	1	28	f	12	6	1	1	5	0	0	1	2	0	2	3	2	2	0	2
10	1	29	t	33	13	4	2	5	1	1	1	2	0	2	3	4	10	1	2
11	1	15	f	10	6	0	1	2	0	0	0	0	0	2	2	2	3	0	1
12	1	1	t	38	28	6	0	3	1	0	4	4	0	4	4	3	5	6	12
13	1	2	t	41	26	3	3	5	2	0	4	0	2	5	7	9	13	1	5
14	1	4	f	22	8	2	4	2	1	0	2	4	1	0	0	4	6	0	1
15	1	6	t	32	13	6	2	6	0	0	0	2	0	4	4	3	6	1	2
16	1	8	t	34	19	1	0	4	1	0	2	5	0	0	0	2	6	5	10
17	1	9	t	31	9	3	2	5	0	2	0	4	0	1	2	4	4	0	0
18	1	13	f	13	9	1	2	2	0	0	0	1	0	0	0	0	6	3	5
19	1	14	f	14	3	4	0	2	0	0	4	2	3	1	2	1	2	0	1
20	2	22	f	17	6	1	0	2	1	0	0	2	0	0	0	0	1	2	4
21	2	23	f	6	3	1	1	0	0	0	0	0	0	0	0	0	0	1	1
22	2	26	t	30	13	6	2	4	1	0	3	0	0	1	2	6	8	0	0
23	2	27	f	9	0	0	1	2	0	0	1	0	1	0	0	0	4	0	0
24	2	29	t	30	15	1	0	4	0	0	3	2	0	4	4	4	5	1	3
25	2	17	f	20	6	0	0	1	0	1	0	5	0	0	0	0	2	2	3
26	2	18	t	35	27	3	0	6	2	1	5	1	2	11	13	8	16	0	3
27	2	19	f	26	9	2	4	3	2	0	1	0	0	1	2	4	6	0	1
28	2	20	t	38	14	3	0	3	1	1	3	2	0	2	2	3	5	2	6
29	2	21	t	19	6	2	1	2	2	0	1	1	0	2	2	2	5	0	2
30	2	28	f	3	2	0	0	1	0	0	1	0	0	0	0	1	1	0	1
31	2	14	f	18	8	1	2	5	1	0	1	2	1	0	0	4	5	0	0
32	2	1	t	36	16	8	0	2	2	0	4	2	0	2	2	4	8	2	11
33	2	3	t	22	12	4	1	5	1	0	1	1	0	1	2	4	5	1	2
34	2	4	f	15	3	2	1	1	0	1	0	0	0	0	0	0	2	1	3
35	2	6	t	34	13	2	1	4	1	0	5	3	2	2	2	4	4	1	3
36	2	8	t	29	12	4	0	1	1	1	3	3	2	0	0	0	2	4	9
37	2	9	f	19	6	3	4	3	3	1	1	2	0	0	0	3	5	0	0
38	2	13	f	7	3	1	0	0	0	1	1	2	0	0	0	0	0	1	1
39	2	15	f	19	8	0	0	1	0	0	0	0	0	0	0	1	2	2	3
40	2	2	t	35	17	4	0	5	0	1	2	2	0	1	3	5	10	2	4
41	3	14	f	16	4	3	1	1	0	0	0	5	0	0	0	2	2	0	0
42	3	10	t	17	11	2	0	2	0	0	0	3	0	1	1	2	2	2	5
43	3	11	f	24	8	1	2	3	0	1	3	2	1	2	2	0	0	2	4
44	3	1	t	35	38	9	1	1	1	0	6	2	1	12	13	4	5	6	13
45	3	16	f	13	10	1	1	2	0	0	1	1	1	0	0	5	6	0	1
46	3	15	f	28	13	3	1	2	1	2	0	0	0	0	0	2	4	3	4
47	3	2	t	36	23	2	0	4	0	1	4	5	0	5	5	6	8	2	5
48	3	9	t	28	9	2	2	6	0	1	2	2	1	5	6	2	2	0	0
49	3	8	t	36	11	6	1	2	1	0	2	2	0	4	4	2	6	1	8
50	3	13	f	1	2	0	0	0	0	0	0	1	0	0	0	1	1	0	0
51	3	22	f	23	12	3	0	3	0	0	1	1	0	0	0	0	1	4	4
52	3	30	f	18	11	1	1	1	0	0	0	3	0	2	2	3	3	1	2
53	3	25	f	20	9	3	1	0	1	1	2	0	0	1	1	1	4	2	4
54	3	27	t	20	2	1	2	2	0	0	1	4	1	0	0	1	4	0	1
55	3	23	f	3	0	0	0	0	0	0	0	0	0	0	0	0	0	0	2
56	3	18	t	39	44	7	0	3	2	1	4	1	0	18	19	13	15	0	1
57	3	28	f	7	2	0	1	1	0	0	1	1	1	0	0	1	2	0	0
58	3	26	t	28	19	7	3	3	0	0	0	4	0	3	3	5	12	2	3
59	3	29	t	32	13	6	1	3	3	0	1	2	1	5	5	4	9	0	1
60	3	20	f	20	18	1	1	0	1	1	0	5	0	3	5	3	3	3	3
61	3	19	t	26	8	0	0	3	2	0	0	2	0	0	0	4	6	0	3
62	4	14	t	10	6	0	0	2	0	0	2	0	0	0	1	3	3	0	1
63	4	16	f	14	2	0	2	0	1	1	0	2	0	2	2	0	1	0	1
64	4	11	f	31	28	0	2	4	0	0	2	4	1	3	3	8	15	3	6
65	4	13	f	21	14	5	1	0	0	0	3	1	0	4	6	2	5	2	4
66	4	7	f	15	11	0	1	4	0	0	0	3	0	0	0	1	3	3	6
67	4	5	t	26	3	5	0	2	0	0	1	2	0	0	0	0	1	1	5
68	4	9	t	32	7	4	2	8	1	6	3	1	1	1	2	3	6	0	0
69	4	10	f	19	4	0	0	0	1	0	1	1	0	2	2	1	4	0	0
70	4	15	t	35	29	3	0	5	0	0	5	3	0	8	11	6	8	3	5
71	4	12	t	32	8	1	0	4	2	0	1	2	1	0	0	1	4	2	4
72	4	31	f	12	4	0	1	0	1	0	1	1	0	0	0	2	3	0	2
73	4	24	f	13	5	0	0	1	1	0	0	2	0	0	0	1	3	1	1
74	4	25	f	14	5	2	1	1	0	0	0	3	0	0	0	1	2	1	4
75	4	27	f	7	0	0	0	1	0	0	1	1	1	0	0	0	1	0	1
76	4	22	f	28	20	5	2	5	2	0	0	2	0	5	5	0	2	5	10
77	4	18	t	35	31	3	2	0	4	0	3	1	0	13	15	9	16	0	1
78	4	26	t	35	17	6	1	10	1	2	2	0	0	0	1	4	7	3	5
79	4	29	t	37	23	4	1	4	2	0	1	1	0	3	3	7	12	2	2
80	4	30	t	26	7	2	2	4	0	0	1	3	0	1	2	3	5	0	3
81	4	20	t	28	6	1	3	3	2	0	2	4	0	2	2	2	8	0	6
\.


--
-- Data for Name: shotdata; Type: TABLE DATA; Schema: app; Owner: okcapplicant
--

COPY app.shotdata (id, player_stats_id, is_make, location_x, location_y) FROM stdin;
180	1	t	0.2	25.1
181	1	t	-7.7	26.1
182	1	f	15.8	24.5
183	1	t	-7.8	23.5
184	1	t	16.3	23.8
185	2	f	-0.2	-0.9
186	2	f	-0.6	0.5
187	2	t	-14.3	0.4
188	2	f	-5.9	13.8
189	2	f	-10.0	11.7
190	2	t	-7.0	13.8
191	2	t	-6.2	5.9
192	2	f	0.9	2.0
193	2	f	-2.0	1.1
194	2	t	0.7	12.7
195	2	t	-18.1	18.0
196	2	f	-1.3	0.8
197	2	f	-6.6	2.0
198	2	t	1.2	10.3
199	2	t	-1.0	13.6
200	2	t	0.1	2.2
201	2	f	0.2	0.8
202	2	f	-6.2	13.0
203	2	f	-14.1	10.3
204	2	f	-6.5	13.8
205	2	t	0.1	2.4
206	2	t	1.0	-0.3
207	2	f	8.7	14.0
208	2	f	7.1	4.0
209	3	f	-14.3	25.3
210	3	t	0.0	0.0
211	3	t	0.4	4.7
212	3	t	13.5	22.5
213	3	f	0.6	0.4
214	3	t	6.9	13.5
215	3	t	23.2	0.8
216	4	f	1.8	24.6
217	4	t	-1.0	0.2
218	4	t	0.7	-0.7
219	4	f	-2.7	1.1
220	4	t	0.6	5.4
221	4	f	23.5	9.7
222	4	f	3.4	0.9
223	4	f	0.0	-0.9
224	5	t	-1.6	0.7
225	5	f	13.5	25.0
226	5	t	0.1	1.2
227	5	t	0.0	0.0
228	5	f	0.0	0.0
229	5	f	-23.0	-1.0
230	5	f	-23.3	4.6
231	5	f	4.0	1.8
232	5	f	-11.9	22.0
233	6	f	-18.3	20.0
234	6	t	-22.8	-1.2
235	6	f	14.5	21.0
236	6	f	-14.1	21.0
237	6	t	-20.5	17.0
238	6	t	-0.7	0.3
239	6	t	1.6	24.6
240	7	f	-22.8	-1.7
241	7	f	22.7	3.3
242	7	f	16.7	24.3
243	8	t	0.0	1.9
244	8	t	1.5	0.9
245	8	f	-22.9	-1.6
246	8	t	-1.6	0.8
247	8	f	-1.3	3.3
248	8	f	-22.5	12.0
249	8	f	23.3	1.4
250	8	t	1.5	-0.7
251	8	f	-7.0	0.9
252	9	f	-22.5	3.2
253	9	f	18.5	19.2
254	9	t	1.5	-0.3
255	9	t	-0.6	2.5
256	10	t	0.5	1.4
257	10	f	-0.9	0.9
258	10	f	-6.7	14.7
259	10	f	-1.6	5.6
260	10	f	8.1	20.9
261	10	t	0.0	0.0
262	10	f	0.0	0.0
263	10	t	1.0	1.9
264	10	f	-18.9	16.6
265	10	t	0.0	0.0
266	10	f	-1.6	0.8
267	10	t	7.7	23.8
268	11	f	21.7	14.1
269	11	t	0.0	0.0
270	11	f	0.5	1.2
271	11	t	-13.6	12.5
272	12	t	-22.4	11.5
273	12	t	1.0	-0.8
274	12	t	0.5	1.3
275	12	f	-23.0	12.5
276	12	t	0.7	-0.1
277	12	f	-20.8	15.0
278	12	f	6.1	7.6
279	12	f	-15.9	23.5
280	12	f	14.7	20.5
281	12	t	16.1	33.9
282	12	t	-21.2	12.3
283	12	f	-19.0	25.0
284	12	t	-16.8	22.2
285	12	t	15.2	20.5
286	12	t	-23.3	2.4
287	12	f	0.9	0.8
288	12	f	-15.9	25.8
289	13	f	22.2	12.1
290	13	f	18.0	1.0
291	13	f	13.5	24.3
292	13	t	23.0	4.4
293	13	t	-0.6	-0.2
294	13	t	-0.1	0.8
295	13	t	0.7	-0.6
296	13	t	7.0	16.0
297	13	t	1.0	-0.2
298	13	f	2.1	0.3
299	13	t	-0.1	2.7
300	13	f	-0.6	2.6
301	13	t	-0.4	1.1
302	13	f	-3.8	20.6
303	13	f	-23.0	1.6
304	13	t	0.2	1.5
305	13	t	0.4	1.4
306	13	f	22.5	0.5
307	14	f	1.0	-0.3
308	14	t	0.0	0.0
309	14	t	0.0	0.0
310	14	f	23.9	9.9
311	14	f	2.7	0.9
312	14	t	-0.9	1.1
313	14	t	-1.2	2.2
314	15	f	6.2	7.2
315	15	f	22.3	4.4
316	15	t	6.2	8.2
317	15	t	-13.1	24.8
318	15	f	-0.1	2.7
319	15	t	1.2	1.5
320	15	t	1.6	2.2
321	15	f	1.1	1.9
322	16	f	-1.8	26.0
323	16	t	-6.0	9.2
324	16	f	-16.8	19.6
325	16	f	-19.6	16.4
326	16	t	16.4	22.8
327	16	t	-16.5	20.7
328	16	f	-15.6	21.9
329	16	t	-16.5	19.0
330	16	t	6.2	6.0
331	16	t	-18.1	17.6
332	16	f	-21.6	14.1
333	16	f	6.1	10.5
334	16	f	-10.8	12.2
335	16	f	6.7	13.5
336	16	t	21.6	14.5
337	16	f	-0.2	2.7
338	17	t	0.0	1.2
339	17	t	0.0	0.0
340	17	t	-0.5	1.9
341	17	t	-6.2	2.0
342	18	f	23.2	0.9
343	18	t	23.2	2.0
344	18	f	6.9	5.9
345	18	t	23.0	2.8
346	18	t	-22.8	-1.2
347	18	f	0.0	0.0
348	18	f	0.0	5.1
349	18	f	17.3	18.4
350	18	f	0.2	0.4
351	18	f	-6.2	5.3
352	18	f	-16.2	-2.2
353	19	f	0.9	2.1
354	19	t	0.9	5.0
355	19	f	-0.4	25.5
356	20	f	-17.0	22.0
357	20	f	2.2	1.5
358	20	f	-17.0	22.4
359	20	t	-8.1	26.0
360	20	t	-8.5	25.5
361	21	t	21.0	13.1
362	22	f	-2.8	11.9
363	22	t	-6.1	4.3
364	22	t	-0.6	6.2
365	22	f	3.6	5.0
366	22	t	1.0	6.0
367	22	t	-6.9	1.3
368	22	t	-1.3	0.9
369	22	t	-2.1	0.7
370	23	f	4.5	0.8
371	23	f	4.5	11.0
372	23	f	-6.0	0.3
373	23	f	-3.2	0.2
374	24	f	-23.9	0.9
375	24	t	-1.3	2.0
376	24	t	-2.3	1.5
377	24	f	-4.2	2.4
378	24	t	-3.8	5.8
379	24	t	-19.5	17.6
380	24	t	3.6	3.3
381	24	f	16.1	20.3
382	25	f	-17.6	0.1
383	25	t	5.6	25.8
384	25	f	23.7	-0.4
385	25	f	-18.4	12.0
386	25	t	-22.5	-3.3
387	26	f	4.8	27.1
388	26	t	-1.8	2.6
389	26	f	3.9	9.3
390	26	f	-5.5	4.3
391	26	f	3.4	7.1
392	26	f	5.8	7.5
393	26	f	3.4	2.0
394	26	t	0.1	6.1
395	26	f	2.7	3.6
396	26	t	-3.7	16.8
397	26	f	-4.3	1.1
398	26	f	2.0	3.1
399	26	t	7.5	12.3
400	26	t	1.8	0.9
401	26	t	15.3	0.5
402	26	f	6.0	26.1
403	26	t	2.7	2.4
404	26	f	14.5	25.9
405	26	t	-2.8	1.0
406	27	t	0.0	0.0
407	27	t	-2.5	12.5
408	27	t	2.0	1.1
409	27	f	-4.7	11.3
410	27	t	0.0	0.0
411	27	f	22.5	12.3
412	27	f	0.6	7.3
413	28	t	1.8	0.6
414	28	f	19.9	15.9
415	28	f	-16.5	22.5
416	28	f	-5.1	4.5
417	28	t	-22.9	2.5
418	28	f	20.6	14.0
419	28	f	-1.5	2.4
420	28	t	0.0	1.8
421	28	t	14.2	23.3
422	28	f	9.3	28.2
423	28	t	-4.0	2.9
424	29	f	2.9	14.3
425	29	f	23.4	-1.6
426	29	t	0.0	0.0
427	29	f	4.7	2.9
428	29	f	22.4	-0.4
429	29	f	-2.0	1.2
430	29	t	3.1	3.3
431	30	t	-0.9	0.3
432	30	f	15.4	21.0
433	31	t	3.8	2.1
434	31	t	0.0	0.0
435	31	t	0.0	0.0
436	31	f	-1.5	9.9
437	31	t	2.8	0.9
438	32	f	-15.7	27.9
439	32	f	-11.6	26.7
440	32	f	-19.6	17.4
441	32	f	-10.3	15.5
442	32	f	3.4	0.9
443	32	f	-15.9	20.7
444	32	f	-18.9	19.2
445	32	f	16.8	22.5
446	32	t	-3.6	5.4
447	32	f	-1.1	25.7
448	32	f	22.2	12.9
449	32	t	-2.6	1.3
450	32	t	11.4	26.6
451	32	f	-16.7	27.6
452	32	t	-7.0	2.4
453	32	t	0.5	28.5
454	32	t	5.5	1.2
455	32	f	-3.8	9.5
456	32	f	-4.2	2.7
457	33	t	-16.3	20.8
458	33	f	-9.3	24.5
459	33	t	12.3	7.1
460	33	t	-2.8	6.2
461	33	t	0.0	0.0
462	33	f	-2.3	2.4
463	33	t	0.9	4.1
464	34	f	-23.7	1.7
465	34	f	-23.2	2.0
466	34	f	-4.5	1.5
467	34	t	-21.6	12.4
468	34	f	2.9	1.4
469	35	t	-2.5	1.6
470	35	f	-22.7	-1.2
471	35	t	1.1	1.5
472	35	t	1.8	3.6
473	35	t	-19.6	16.4
474	35	t	1.8	1.2
475	35	f	-23.0	1.4
476	36	t	-15.9	20.9
477	36	t	-23.0	1.2
478	36	f	4.2	3.4
479	36	f	-17.6	20.6
480	36	f	23.0	3.5
481	36	f	-17.4	18.3
482	36	t	13.6	23.1
483	36	t	-23.7	8.8
484	36	f	-6.4	8.7
485	36	f	-2.1	26.7
486	36	f	-24.1	7.9
487	37	t	1.2	2.1
488	37	f	-2.5	3.8
489	37	f	9.3	-0.2
490	37	t	1.0	2.0
491	37	t	2.2	1.5
492	38	t	9.9	24.5
493	39	t	-2.5	1.9
494	39	f	-15.2	22.3
495	39	f	-14.8	14.6
496	39	t	22.9	0.0
497	39	t	-23.3	8.2
498	40	t	2.2	1.2
499	40	t	-1.6	2.0
500	40	t	18.4	21.3
501	40	f	-16.5	5.5
502	40	t	-3.1	2.8
503	40	f	1.8	2.8
504	40	t	1.7	2.4
505	40	f	9.3	24.9
506	40	f	0.7	5.5
507	40	f	0.0	40.3
508	40	t	-3.8	4.2
509	40	t	23.0	0.1
510	40	f	-4.7	2.6
511	40	f	11.8	4.7
512	41	t	2.1	0.7
513	41	t	-0.1	1.0
514	42	f	21.6	11.1
515	42	f	-22.8	1.5
516	42	t	-6.6	2.0
517	42	t	16.3	20.3
518	42	t	-21.1	16.7
519	42	f	22.4	5.1
520	42	t	-1.1	-0.5
521	43	f	11.2	24.7
522	43	t	12.0	24.6
523	43	f	14.3	22.6
524	43	t	16.3	21.0
525	44	t	11.8	14.3
526	44	t	-0.1	29.3
527	44	f	16.1	22.4
528	44	t	10.5	25.2
529	44	f	2.5	1.9
530	44	f	-9.3	25.4
531	44	t	-0.5	-0.2
532	44	t	-0.7	0.2
533	44	f	14.3	27.5
534	44	t	7.8	25.6
535	44	t	-5.8	26.1
536	44	f	-14.6	24.4
537	44	t	-18.1	23.6
538	44	f	-11.3	26.0
539	44	f	23.3	1.2
540	44	t	-14.8	22.7
541	44	f	14.7	23.9
542	44	t	0.0	0.4
543	45	t	0.7	0.3
544	45	t	-8.8	13.5
545	45	t	-9.9	-1.0
546	45	t	0.2	-0.2
547	45	f	-23.3	-0.7
548	45	f	-0.7	0.3
549	45	t	0.2	-0.7
550	46	f	1.2	1.4
551	46	t	-0.7	1.0
552	46	t	-18.3	17.3
553	46	t	23.8	2.5
554	46	t	-17.5	19.4
555	46	t	-0.2	0.3
556	46	f	-15.4	2.6
557	46	f	-17.2	19.9
558	47	t	11.6	3.3
559	47	f	22.4	4.2
560	47	f	17.6	17.5
561	47	t	21.4	1.4
562	47	t	0.2	-0.2
563	47	t	20.8	16.6
564	47	t	0.9	0.6
565	47	f	1.0	-0.1
566	47	f	-23.3	2.4
567	47	t	-22.7	6.2
568	47	t	0.1	-1.7
569	47	t	0.5	12.9
570	47	f	-13.1	4.6
571	48	t	5.9	3.0
572	48	t	1.0	0.9
573	49	f	18.6	21.2
574	49	f	-23.0	-0.1
575	49	f	-22.7	11.4
576	49	f	11.9	24.1
577	49	t	1.1	29.7
578	49	f	6.2	6.3
579	49	t	0.2	1.5
580	49	f	2.0	1.2
581	49	f	-15.8	23.3
582	49	f	-2.0	6.4
583	49	f	-15.7	22.7
584	49	f	-0.1	9.4
585	49	f	18.4	16.7
586	49	t	-1.1	0.8
587	50	t	1.3	0.5
588	51	t	8.3	25.3
589	51	t	22.8	0.5
590	51	f	1.6	0.0
591	51	t	-16.7	24.6
592	51	t	-22.5	1.8
593	52	t	0.6	-0.5
594	52	f	-0.2	25.0
595	52	t	1.1	0.9
596	52	t	-23.2	7.0
597	52	t	-6.1	12.5
598	53	f	15.3	20.4
599	53	f	1.7	0.3
600	53	f	-5.6	3.9
601	53	t	0.4	-0.2
602	53	f	0.0	0.0
603	53	f	-15.6	27.1
604	53	t	17.5	23.6
605	53	t	-22.9	10.2
606	54	f	0.7	0.5
607	54	t	-0.6	1.1
608	54	f	13.5	25.1
609	54	f	0.0	0.0
610	54	f	2.5	1.3
611	55	f	-13.7	24.3
612	55	f	-20.7	16.7
613	56	t	1.0	0.7
614	56	f	-21.7	11.2
615	56	t	2.7	0.9
616	56	t	-8.0	8.9
617	56	t	-0.4	1.0
618	56	f	13.1	-1.1
619	56	t	0.9	1.2
620	56	t	-1.0	0.0
621	56	t	-0.6	0.3
622	56	t	-0.7	-1.2
623	56	t	0.1	0.8
624	56	f	2.3	0.9
625	56	t	0.2	1.3
626	56	t	-1.3	-0.2
627	56	t	-2.8	0.5
628	56	t	0.5	0.7
629	57	t	-1.1	1.3
630	57	f	0.0	0.0
631	58	f	5.8	2.6
632	58	t	-18.8	16.1
633	58	t	-6.9	11.1
634	58	t	-16.8	22.7
635	58	t	-0.5	2.4
636	58	f	-4.5	7.1
637	58	f	-1.6	4.4
638	58	f	-15.6	22.5
639	58	t	-2.3	-0.5
640	58	t	1.0	6.2
641	58	f	3.8	3.1
642	58	f	-8.9	4.0
643	58	t	-0.4	1.4
644	58	f	0.0	0.0
645	58	f	-1.0	0.8
646	59	f	-5.1	4.2
647	59	t	-0.2	1.2
648	59	t	1.8	0.6
649	59	f	1.2	0.6
650	59	f	22.9	5.2
651	59	f	-1.2	-0.4
652	59	f	4.4	21.3
653	59	t	1.1	1.7
654	59	t	0.2	0.8
655	59	f	1.8	0.8
656	60	t	-0.5	1.9
657	60	t	-23.0	4.1
658	60	t	-0.9	-0.1
659	60	t	-15.4	27.3
660	60	t	-0.4	0.8
661	60	t	-10.2	26.7
662	61	f	-23.5	4.6
663	61	t	-1.5	-1.1
664	61	f	-3.4	27.6
665	61	f	2.8	13.4
666	61	t	-1.1	-0.4
667	61	t	0.5	1.2
668	61	t	2.6	1.3
669	61	f	9.7	26.5
670	61	f	1.8	0.5
671	62	f	21.0	13.4
672	62	t	-2.1	0.3
673	62	t	7.1	0.4
674	62	t	0.2	4.6
675	63	f	22.3	0.6
676	63	f	1.2	0.8
677	64	f	-2.3	1.9
678	64	t	0.0	0.0
679	64	f	-0.5	1.5
680	64	f	19.5	44.0
681	64	t	12.9	24.0
682	64	f	16.9	22.4
683	64	f	11.0	18.2
684	64	f	3.9	16.9
685	64	t	7.7	14.7
686	64	f	-7.8	19.6
687	64	t	-17.4	22.9
688	64	f	-16.7	18.9
689	64	t	-20.6	14.4
690	64	t	2.0	-0.1
691	64	t	0.0	3.6
692	64	t	1.2	1.7
693	64	f	-3.7	1.3
694	64	t	-0.6	0.9
695	64	t	0.1	0.4
696	64	t	-0.7	5.9
697	64	f	-2.3	5.0
698	65	t	12.5	23.6
699	65	t	-10.8	25.1
700	65	f	-1.3	0.7
701	65	t	-1.2	-0.6
702	65	t	1.7	0.2
703	65	f	2.7	6.3
704	65	f	5.4	2.8
705	65	f	-23.4	1.5
706	65	f	-23.0	0.5
707	66	f	12.1	26.1
708	66	t	-6.9	20.4
709	66	t	-18.8	18.3
710	66	t	-17.5	19.0
711	66	t	23.3	-0.1
712	66	f	22.4	1.9
713	66	f	23.2	3.4
714	66	f	-1.3	0.5
715	66	f	3.6	2.4
716	67	f	-3.8	25.8
717	67	f	9.7	23.4
718	67	f	16.9	20.4
719	67	f	1.0	21.0
720	67	f	-17.2	19.7
721	67	t	-17.2	19.2
722	68	f	1.8	0.3
723	68	t	0.0	0.0
724	68	t	-0.4	1.9
725	68	f	-1.6	1.5
726	68	f	-1.3	1.2
727	68	t	1.6	1.2
728	69	f	-7.2	10.5
729	69	f	10.2	1.1
730	69	t	-0.7	0.2
731	69	f	-7.4	3.4
732	70	t	16.5	23.9
733	70	f	12.9	9.4
734	70	t	-3.6	14.3
735	70	t	0.5	21.5
736	70	t	-23.5	9.5
737	70	f	-22.6	7.9
738	70	t	-22.7	12.4
739	70	f	-21.9	13.0
740	70	t	1.7	0.0
741	70	t	0.6	1.5
742	70	f	1.1	0.5
743	70	t	5.0	4.1
744	70	t	-6.1	3.4
745	71	f	18.3	15.8
746	71	t	16.5	22.9
747	71	t	-16.8	19.0
748	71	f	22.8	2.5
749	71	t	1.6	0.6
750	71	f	-1.6	1.2
751	71	f	-1.8	0.4
752	71	f	6.9	0.6
753	72	f	2.0	0.5
754	72	f	-0.4	26.1
755	72	f	-20.5	15.7
756	72	t	1.0	0.3
757	72	t	-0.7	0.3
758	73	f	2.7	16.7
759	73	t	-21.9	10.8
760	73	f	-1.2	0.4
761	73	t	1.7	0.6
762	74	f	-17.0	21.5
763	74	f	-12.6	22.5
764	74	f	-21.2	14.5
765	74	f	-1.8	1.0
766	74	t	1.7	0.5
767	74	t	-22.3	0.4
768	75	f	2.6	1.2
769	75	f	-22.1	-0.2
770	76	f	1.0	1.2
771	76	f	-6.7	26.1
772	76	t	21.3	13.6
773	76	f	-20.2	16.2
774	76	t	-20.6	17.3
775	76	t	-19.0	16.5
776	76	t	-18.4	19.8
777	76	f	-15.4	23.6
778	76	f	-22.9	8.0
779	76	f	-19.5	17.8
780	76	t	23.7	2.1
781	76	f	1.6	0.7
782	77	f	-1.8	0.6
783	77	t	7.2	5.9
784	77	f	-3.6	26.8
785	77	f	-2.7	15.9
786	77	f	15.9	2.1
787	77	t	0.7	1.2
788	77	t	-0.4	1.4
789	77	f	1.3	1.0
790	77	t	-0.2	0.2
791	77	f	1.7	0.8
792	77	t	-0.5	0.1
793	77	t	-1.1	1.2
794	77	f	-1.2	1.2
795	77	t	-1.7	1.2
796	77	t	-0.9	1.2
797	77	f	0.9	2.8
798	77	t	-1.1	7.7
799	78	f	-0.4	8.3
800	78	f	18.5	16.8
801	78	t	19.0	18.9
802	78	t	-23.2	9.9
803	78	f	-21.8	11.9
804	78	t	-16.3	21.9
805	78	t	0.4	1.0
806	78	t	0.6	0.2
807	78	f	-0.7	2.9
808	78	f	-2.0	0.1
809	78	t	4.8	5.0
810	78	t	7.4	5.7
811	79	f	0.9	-0.2
812	79	f	0.0	1.0
813	79	f	8.0	12.4
814	79	t	-16.2	20.1
815	79	t	-14.7	23.9
816	79	t	-0.5	0.8
817	79	t	0.4	1.5
818	79	t	0.6	0.4
819	79	t	0.0	1.2
820	79	f	-0.2	2.2
821	79	t	-0.6	0.9
822	79	t	-1.2	5.4
823	79	f	-1.7	5.9
824	79	t	-19.9	-2.2
825	80	t	0.0	0.0
826	80	f	12.1	22.2
827	80	f	20.2	15.8
828	80	f	14.5	21.0
829	80	t	-7.1	8.8
830	80	f	2.2	0.1
831	80	f	0.7	1.4
832	80	t	-0.2	0.6
833	81	f	0.0	0.0
834	81	f	-2.7	1.0
835	81	t	-0.1	0.1
836	81	f	12.3	25.9
837	81	f	10.4	26.0
838	81	f	9.9	24.1
839	81	f	1.3	8.9
840	81	f	0.1	8.7
841	81	f	-16.3	21.5
842	81	f	23.4	5.1
843	81	t	-1.3	-0.1
844	81	f	2.3	4.0
845	81	f	-4.0	0.1
846	81	f	-22.8	0.4
\.


--
-- Data for Name: teams; Type: TABLE DATA; Schema: app; Owner: okcapplicant
--

COPY app.teams (id, name) FROM stdin;
1	Tune Squad
2	Monstars
\.


--
-- Name: games_id_seq; Type: SEQUENCE SET; Schema: app; Owner: okcapplicant
--

SELECT pg_catalog.setval('app.games_id_seq', 1, false);


--
-- Name: players_id_seq; Type: SEQUENCE SET; Schema: app; Owner: okcapplicant
--

SELECT pg_catalog.setval('app.players_id_seq', 1, false);


--
-- Name: playerstats_id_seq; Type: SEQUENCE SET; Schema: app; Owner: okcapplicant
--

SELECT pg_catalog.setval('app.playerstats_id_seq', 3, true);


--
-- Name: shotdata_id_seq; Type: SEQUENCE SET; Schema: app; Owner: okcapplicant
--

SELECT pg_catalog.setval('app.shotdata_id_seq', 1198, true);


--
-- Name: teams_id_seq; Type: SEQUENCE SET; Schema: app; Owner: okcapplicant
--

SELECT pg_catalog.setval('app.teams_id_seq', 1, false);


--
-- Name: games games_pkey; Type: CONSTRAINT; Schema: app; Owner: okcapplicant
--

ALTER TABLE ONLY app.games
    ADD CONSTRAINT games_pkey PRIMARY KEY (id);


--
-- Name: players players_pkey; Type: CONSTRAINT; Schema: app; Owner: okcapplicant
--

ALTER TABLE ONLY app.players
    ADD CONSTRAINT players_pkey PRIMARY KEY (id);


--
-- Name: playerstats playerstats_pkey; Type: CONSTRAINT; Schema: app; Owner: okcapplicant
--

ALTER TABLE ONLY app.playerstats
    ADD CONSTRAINT playerstats_pkey PRIMARY KEY (id);


--
-- Name: shotdata shotdata_pkey; Type: CONSTRAINT; Schema: app; Owner: okcapplicant
--

ALTER TABLE ONLY app.shotdata
    ADD CONSTRAINT shotdata_pkey PRIMARY KEY (id);


--
-- Name: teams teams_pkey; Type: CONSTRAINT; Schema: app; Owner: okcapplicant
--

ALTER TABLE ONLY app.teams
    ADD CONSTRAINT teams_pkey PRIMARY KEY (id);


--
-- Name: games games_away_team_id_fkey; Type: FK CONSTRAINT; Schema: app; Owner: okcapplicant
--

ALTER TABLE ONLY app.games
    ADD CONSTRAINT games_away_team_id_fkey FOREIGN KEY (away_team_id) REFERENCES app.teams(id);


--
-- Name: games games_home_team_id_fkey; Type: FK CONSTRAINT; Schema: app; Owner: okcapplicant
--

ALTER TABLE ONLY app.games
    ADD CONSTRAINT games_home_team_id_fkey FOREIGN KEY (home_team_id) REFERENCES app.teams(id);


--
-- Name: playerstats playerstats_game_id_fkey; Type: FK CONSTRAINT; Schema: app; Owner: okcapplicant
--

ALTER TABLE ONLY app.playerstats
    ADD CONSTRAINT playerstats_game_id_fkey FOREIGN KEY (game_id) REFERENCES app.games(id);


--
-- Name: playerstats playerstats_player_id_fkey; Type: FK CONSTRAINT; Schema: app; Owner: okcapplicant
--

ALTER TABLE ONLY app.playerstats
    ADD CONSTRAINT playerstats_player_id_fkey FOREIGN KEY (player_id) REFERENCES app.players(id);


--
-- Name: shotdata shotdata_player_stats_id_fkey; Type: FK CONSTRAINT; Schema: app; Owner: okcapplicant
--

ALTER TABLE ONLY app.shotdata
    ADD CONSTRAINT shotdata_player_stats_id_fkey FOREIGN KEY (player_stats_id) REFERENCES app.playerstats(id);


--
-- Name: SCHEMA app; Type: ACL; Schema: -; Owner: postgres
--

GRANT ALL ON SCHEMA app TO okcapplicant;


--
-- PostgreSQL database dump complete
--

