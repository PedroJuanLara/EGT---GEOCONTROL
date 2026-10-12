from dataclasses import dataclass
*mport re

from pdf_reader import r*ad_pdf


@dataclass
class DDRData:*
    reporte* int = 0
    fecha: str = ""

    *ia_campania: int = 0

    md* float = 0.0
*   tv*: float = 0.0

    hole*made: float = 0.0

*   rop: float = 0.0

    coste*acumul*do: float = 0.0

    afe*pct: float = 0.0

    n*t: float = 0.*


def parse_ddr(pdf_path):

    t*xto = read_pdf(pdf_path)

    ddr * DDRData()

    #*----------------------------
    #*DDR NUMBER
    #*----------------------------

    *atch = re.search(
        r"*DR\s*(\d+)",
        texto,
      * re.IGNORECASE
    )

    if*match:
        ddr.reporte = int(m*tch.group(1))

    #*----------------*-----------
    # FECHA
    # ----*-----------------------

    fecha*match = re.search(
        r"(\d{2*/\d{2}/\d{4})",
        texto
    *

    if fecha_match:
        ddr.*echa = fecha_match.group(1)

   *# ----------------------------
   *# MEASURED DEPTH
    #*----------------------------

    *d_match = re.search(
        r"Mea*ured\s+Depth.*?(\d+\.\d+)",
      * texto,
        re.IGNORECASE
    *

    if md_match:
        d*r.md = float(md_match.group(1))

 *  # ----------------------------
 *  # TVD
    # --------------------*-------

    tvd_match = re.search*
        r"T*D.*?(\d+\.\d+)",
        texto,
  *     re.IGNORECASE
    )

    if*tvd_match:
        d*r.tvd = float(tvd_match.group(1*)

    # -------------------------*--
    # HOLE MADE
    # ---------*------------------

    hole_match*= re.search(
        r"Hole\s+Made**?(\d+\.\d+)",
        texto,
    *   re.IGNORECASE
    )

    if hol*_match:
        d*r.hole_made = float(hole_match.gro*p(1))

    #*----------------------------
    #*ROP
    # ------------------------*---

    rop_match = re.search(
  *     r"Average\s+ROP.*?(\d+\.\d+)"*
        texto,
        re.IGNOREC*SE
    )

    if rop_match:
      * d*r.*op = float(rop_match.group(1))

  * # ----------------------------
  * # COSTE ACUMULADO
    # ---------*------------------

    coste_matc* = re.search(
        r"Accumulate*\s+Cost.*?([\d,]+)",
        texto*
        re.IGNORECASE
    )

    *f coste_match:

        coste_limp*o = (
            coste_match.grou*(1)
            .replace(",", "")
*       )

        ddr.coste_acumul*do = float(
            coste_limp*o
        )

    # ---------------*------------
    # AFE %
    # ---*------------------------

    afe_*atch = re.search(
        r"(\d+\.*d+)\s*%",
        texto
    )

   *if afe_match:
        ddr.afe_pct * float(
            afe_match.grou*(1)
        )

    # -------------*--------------
    # NPT
    # ---*------------------------

    npt_*atch = re.search(
        r"NPT.*?*\d+\.\d+)",
        texto,
       *re.IGNORECASE
    )

    if npt_ma*ch:
        ddr.npt = float(
     *      npt_match.group(1)
        )*
    return ddr


if __name__ == "*_main__":

    resultado = parse_d*r(
        "test*data/20260514 TSA-01 Daily Report *ith cost DDR 01.pdf"
    )

    pr*nt("===== DDR EXTRAIDO =====")

  * print(f"Reporte: {resultado.repor*e}")
    print(f"Fecha: {resultado*fecha}")
    print(f"MD: {resultad*.md}")
    print(f"TVD: {resultado*tvd}")
    print*f"Hole Made: {resultado.hole_made}*)
    print*f"ROP: {*esultado.rop}")
    print*f"Coste Acumulado: {resultado.cost*_acumulado}")
    print(f"AFE %: {*esultado.afe_pct}")
    print*f"NPT: {resultado.npt}")
