CREATE TABLE sondeos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT,
    nombre TEXT,
    estado TEXT,
    fecha_inicio DATE,
    fecha_fin DATE,
    profundidad_objetivo REAL,
    presupuesto_objetivo REAL,
    dias_objetivo INTEGER
);

CREATE TABLE reportes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sondeo_id INTEGER,
    numero_reporte INTEGER,
    fecha DATE,
    dia_campania INTEGER,
    resumen TEXT,
    pdf_original TEXT
);
