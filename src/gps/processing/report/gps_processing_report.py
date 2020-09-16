# -*- coding: utf-8 -*-
"""
/***************************************************************************
        COLPOS: Colombian online GPS data processing service
        ------------------------------------------------------------
        begin                : 2020-09-01
        git sha              : :%H$
        copyright            : (C) 2020 by Leo Cardona
        email                : leo.cardona.p@gmail.com
 ***************************************************************************/
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License v3.0 as          *
 *   published by the Free Software Foundation.                            *
 *                                                                         *
 ***************************************************************************/
"""
from fpdf import FPDF, HTMLMixin

pdf_w = 210
pdf_h = 297


class GPSProcessingReport(FPDF, HTMLMixin):
    def header(self):
        self.rect(5.0, 5.0, 200.0, 287.0)  # Add margin
        self.set_author('Leonardo Cardona')

        # Add report title
        self.set_xy(0.0, 0.0)
        self.set_font('Arial', 'B', 16)
        self.set_text_color(0, 0, 0)
        self.cell(w=210.0, h=40.0, align='C', txt="Reporte de procesamiento GPS", border=0)

    def intro(self):
        msg = 'Este documento es un reporte de procesamiento de datos GPS realizado utilizado el servicio web COLPOS (versión 0.0.1). El servicio de procesamiento online utiliza los productos del Servicio Internacional GNSS (IGS) (final, rápido, ultrarrápido según la disponibilidad) para calcular coordenadas precisas en ITRF en cualquier lugar de la Tierra. Este servicio está diseñado para procesar solo datos GPS doble frecuencia.'

        self.set_xy(10.0, 30)
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, msg)

    def add_coordinates_result(self, station, lat, lon, height, sdn, sde, sdu):
        self.set_xy(10.0, 90)
        self.set_font('Arial', '', 12)
        html = """
                <p><b>Coordenadas geodésicas, Elipsoide GRS80, ITRF2014</b></p>
                <table border="1" align="center" width="100%">
                <thead>
                    <tr>
                        <th width="25%">Estación</th>
                        <th width="25%">Latitud (DMS)</th>
                        <th width="25%">Longitud (DMS)</th>
                        <th width="25%">Altura Elipsoidal (m)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>{station}</td>
                        <td>{latitude}</td>
                        <td>{longitude}</td>
                        <td>{height_ellipsoidal}</td>
                    </tr>
                </tbody>
            </table>
            <p><b>Incertidumbre posicional (95% C.L.)</b></p>
            <table border="1" align="center" width="100%">
                <thead>
                    <tr>
                        <th width="25%">Estación</th>
                        <th width="25%">Norte (Lat) (cm)</th>
                        <th width="25%">Este (Lon) (cm)</th>
                        <th width="25%">Vertical (cm)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>{station}</td>
                        <td>{sdn}</td>
                        <td>{sde}</td>
                        <td>{sdu}</td>
                    </tr>
                </tbody>
            </table>
                """.format(station=station,
                           latitude=lat,
                           longitude=lon,
                           height_ellipsoidal=height,
                           sdn=sdn,
                           sde=sde,
                           sdu=sdu)

        self.write_html(html)

    def add_computation_standards(self):
        self.add_page()
        self.set_xy(10, 30)
        self.set_font('Arial', '', 12)
        html = """
            <p><b>Coordenadas geodésicas, Elipsoide GRS80, ITRF2014</b></p>
            <table border="1" align="center" width="100%">
                <thead>
                    <tr>
                        <th width="25%"> </th>
                        <th width="75%">Descripción</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Software</strong></td>
                        <td>RTKLib versión 2.4.3 b33</td>
                    </tr>
                    <tr>
                        <td>Sistema GNSS</td>
                        <td>Constelación GPS </td>
                    </tr>
                </tbody>
            </table>
            <p><b>Incertidumbre posicional (95% C.L.)</b></p>
            <table border="1" align="center" width="100%">
                <thead>
                    <tr>
                        <th width="25%"> </th>
                        <th width="75%">Descripción</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Modo de posicionamiento</td>
                        <td>PPP Estático </td>
                    </tr>
                    <tr>
                        <td>Frecuencias</td>
                        <td>L1 + L2</td>
                    </tr>
                    <tr>
                        <td>Mascara de elevación</td>
                        <td>10º</td>
                    </tr>
                    <tr>
                        <td>Corrección por mareas</td>
                        <td>Solid/OTL</td>
                    </tr>
                    <tr>
                        <td>Corrección ionosférica</td>
                        <td>Estimación TEC (Contenido total de electrones)</td>
                    </tr>
                    <tr>
                        <td>Corrección troposférica</td>
                        <td>Estimación ZTD (Retardo Cenital Troposférico Total) + Grad</td>
                    </tr>
                    <tr>
                        <td>Orbitas/Relojes</td>
                        <td>Los mejores productos IGS disponibles.</td>
                    </tr>
                    <tr>
                        <td>Orientación de la tierra</td>
                        <td>Los mejores productos IGS disponibles.</td>
                    </tr>
                    <tr>
                        <td>Fase de la antena</td>
                        <td>Se aplica el modelo de variación absoluta de centro de fase IGS14.</td>
                    </tr>
                </tbody>
            </table>
            <p><b>Marco de referencia e incertidumbre de las coordenadas</b></p>
            <table border="1" align="center" width="100%">
                <thead>
                    <tr>
                        <th width="25%"> </th>
                        <th width="75%">Descripción</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Incertidumbre</td>
                        <td>Nivel de confianza del 95% para ITRF2014.</td>
                    </tr>
                    <tr>
                        <td>Datum</td>
                        <td>WGS84</td>
                    </tr>
                </tbody>
            </table>
            """
        self.write_html(html)

    def image_processing(self, location_img):
        self.add_page()
        self.set_xy(30, 30)
        self.image(location_img, link='', type='', w=160, h=140)

    def footer(self):
        """
        Footer on each page
        """
        # position footer at 15mm from the bottom
        self.set_y(-15)

        # set the font, I=italic
        self.set_font("Arial", style="I", size=8)

        # display the page number and center it
        page_num = "Page {}".format(self.page_no())
        self.cell(0, 10, page_num, align="C")
