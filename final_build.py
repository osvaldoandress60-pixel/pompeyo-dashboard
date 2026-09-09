#!/usr/bin/env python3
import json

# Leer datos
with open('cpd_data_v3.json', 'r', encoding='utf-8') as f:
    datos = json.load(f)

# Crear HTML embebiendo JSON en múltiples líneas
html_header = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Control Entregas Vehiculos a CPD</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        :root { --navy: #1a3a6b; --celeste: #2563a8; --gris-claro: #f0f3f8; --rojo: #d32f2f; --verde: #2e7d32; }
        body { font-family: Segoe UI, sans-serif; background: linear-gradient(135deg, #1a3a6b 0%, #0f2847 100%); color: #1a1f2e; min-height: 100vh; padding: 20px; }
        .container { max-width: 1800px; margin: 0 auto; }
        .header { background: linear-gradient(135deg, #1a3a6b 0%, #0f2847 100%); color: white; padding: 30px 40px; border-radius: 12px; margin-bottom: 30px; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3); }
        .header h1 { font-size: 2em; margin-bottom: 8px; }
        .header p { font-size: 0.9em; opacity: 0.9; }
        .resumen-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 15px; margin-bottom: 30px; }
        .card-stat { background: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); border-left: 4px solid var(--celeste); }
        .card-stat h3 { font-size: 0.75em; color: #1a1f2e; margin-bottom: 8px; text-transform: uppercase; }
        .card-stat .valor { font-size: 1.8em; font-weight: bold; color: var(--navy); }
        .filtros-section { background: white; padding: 20px; border-radius: 10px; margin-bottom: 30px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); }
        .filtros-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; margin-bottom: 15px; }
        select, input { width: 100%; padding: 8px 12px; border: 1px solid #d1d9e6; border-radius: 6px; }
        button { padding: 10px 16px; border: none; border-radius: 6px; cursor: pointer; font-weight: 500; margin-right: 10px; }
        .btn-primary { background: var(--celeste); color: white; }
        .btn-secondary { background: var(--gris-claro); color: var(--navy); }
        .btn-success { background: var(--verde); color: white; }
        .alertas-section { background: white; padding: 20px; border-radius: 10px; margin-bottom: 30px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); }
        .table-container { background: white; border-radius: 10px; overflow-x: auto; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); margin-bottom: 30px; }
        table { width: 100%; border-collapse: collapse; font-size: 0.9em; }
        th { background: var(--navy); color: white; padding: 12px; text-align: left; font-weight: 600; position: sticky; top: 0; }
        td { padding: 12px; border-bottom: 1px solid var(--gris-claro); }
        tr:hover { background: var(--gris-claro); }
        .modal { display: none; position: fixed; z-index: 1000; left: 0; top: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.5); }
        .modal.show { display: flex; align-items: center; justify-content: center; }
        .modal-content { background: white; padding: 30px; border-radius: 12px; max-width: 600px; width: 90%; max-height: 85vh; overflow-y: auto; }
        .form-group { margin-bottom: 15px; }
        .form-group label { display: block; margin-bottom: 5px; font-weight: 600; color: var(--navy); }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div>
                <h1>📊 Control Entregas Vehiculos a CPD</h1>
                <p>Pompeyo Carrasco - Gestión de Distribución</p>
                <p style="font-size: 0.8em; opacity: 0.8;">429 vehiculos entregados</p>
            </div>
            <div style="text-align: center; padding: 10px;">
                <img src="pompeyo_logo_blanco.png" alt="POMPEYO" style="max-height: 80px; max-width: 150px;">
            </div>
        </div>

        <div class="resumen-grid" id="resumen-grid"></div>

        <div class="filtros-section">
            <h3>🔍 Filtros Avanzados</h3>
            <div class="filtros-grid">
                <div><label>Marca</label><select id="filtro-marca"><option value="">Todas</option></select></div>
                <div><label>Gerencia</label><select id="filtro-gerencia"><option value="">Todas</option><option value="DC">DC</option><option value="NB">NB</option></select></div>
                <div><label>Categoria</label><select id="filtro-categoria"><option value="">Todas</option><option value="RENTING">RENTING</option><option value="TEST CAR">TEST CAR</option><option value="COMPANY CAR">COMPANY CAR</option><option value="OTROS">OTROS</option></select></div>
                <div><label>Fecha Entrega</label><input type="date" id="filtro-fecha-entrega" placeholder="Desde..."></div>
                <div><label>Copia Llave</label><select id="filtro-llave"><option value="">Todas</option><option value="si">Con Llave</option><option value="no">Sin Llave</option></select></div>
                <div><label>FED</label><select id="filtro-fed"><option value="">Todas</option><option value="si">Con FED</option><option value="no">Sin FED</option></select></div>
                <div><label>Genesis</label><select id="filtro-genesis"><option value="">Todas</option><option value="Ok">Ok</option><option value="Sin">Sin Confirmar</option></select></div>
                <div><label>Busqueda</label><input type="text" id="filtro-busqueda" placeholder="Patente..."></div>
            </div>
            <div>
                <button class="btn-primary" onclick="aplicarFiltros()">Aplicar</button>
                <button class="btn-secondary" onclick="limpiarFiltros()">Limpiar</button>
                <button class="btn-success" onclick="abrirModalNuevo()">+ Agregar</button>
            </div>
        </div>

        <div class="alertas-section" id="alertas-section"></div>

        <div class="table-container">
            <table id="tabla-vehiculos">
                <thead>
                    <tr>
                        <th>Accion</th><th>Patente</th><th>Marca</th><th>Gerencia</th><th>Modelo</th><th>Categoria</th><th>Fecha Entrega</th><th>Numero Factura</th><th>Llave</th><th>FED</th><th>Genesis</th><th>Sol Precio</th><th>Ent Precio</th><th>Sol Factura</th><th>Factura</th>
                        <th style="background: #c8e6c9; white-space: normal; max-width: 100px;" title="Solicitud Precio → Entrega Precio">📅 SLA1<div style="font-size: 0.65em; line-height: 1.2;">Solicitud→Entrega</div></th>
                        <th style="background: #ffe0b2; white-space: normal; max-width: 100px;" title="Entrega Precio → Solicitud Factura">⏰ SLA2<div style="font-size: 0.65em; line-height: 1.2;">Entrega→Solicitud</div></th>
                        <th style="background: #bbdefb; white-space: normal; max-width: 100px;" title="Solicitud Factura → Factura CND">📬 SLA3<div style="font-size: 0.65em; line-height: 1.2;">Solicitud→Factura</div></th>
                    </tr>
                </thead>
                <tbody id="tabla-body"></tbody>
            </table>
        </div>
    </div>

    <div id="modalEditar" class="modal">
        <div class="modal-content">
            <h2>Editar</h2>
            <form id="formEditar" onsubmit="guardarEdicion(event)">
                <div class="form-group"><label>Patente</label><input type="text" id="edit-patente" readonly></div>
                <div class="form-group"><label>Numero Factura</label><input type="text" id="edit-numero-factura"></div>
                <div class="form-group"><label>Factura SI/NO</label><select id="edit-factura-sino"><option value="">Seleccionar</option><option value="si">SI</option><option value="no">NO</option></select></div>
                <div class="form-group"><label>Copia Llave</label><input type="text" id="edit-copia-llave"></div>
                <div class="form-group"><label>FED</label><input type="text" id="edit-fed"></div>
                <div class="form-group"><label>Genesis</label><select id="edit-genesis"><option value="">Seleccionar</option><option value="Ok">Ok</option><option value="En Renting">En Renting</option></select></div>
                <div class="form-group"><label>Solicitud Precio</label><input type="date" id="edit-fecha-sol-precio"></div>
                <div class="form-group"><label>Entrega Precio</label><input type="date" id="edit-fecha-entrega-precio"></div>
                <div class="form-group"><label>Solicitud Factura CND</label><input type="date" id="edit-fecha-sol-factura"></div>
                <div class="form-group"><label>Factura CND</label><input type="date" id="edit-fecha-factura"></div>
                <button type="submit" class="btn-primary">Guardar</button>
                <button type="button" class="btn-secondary" onclick="cerrarModal('modalEditar')">Cancelar</button>
            </form>
        </div>
    </div>

    <div id="modalNuevo" class="modal">
        <div class="modal-content">
            <h2>Agregar Vehiculo</h2>
            <form id="formNuevo" onsubmit="agregarVehiculo(event)">
                <div class="form-group"><label>Patente *</label><input type="text" id="new-patente" required></div>
                <div class="form-group"><label>Marca *</label><select id="new-marca" required></select></div>
                <div class="form-group"><label>Modelo *</label><input type="text" id="new-modelo" required></div>
                <div class="form-group"><label>VIN *</label><input type="text" id="new-vin" required></div>
                <div class="form-group"><label>Categoria *</label><select id="new-categoria" required><option value="">Seleccionar</option><option value="RENTING">RENTING</option><option value="TEST CAR">TEST CAR</option><option value="COMPANY CAR">COMPANY CAR</option><option value="OTROS">OTROS</option></select></div>
                <div class="form-group"><label>Fecha Entrega *</label><input type="date" id="new-fecha-entrega" required></div>
                <div class="form-group"><label>Numero Factura</label><input type="text" id="new-numero-factura"></div>
                <div class="form-group"><label>Factura SI/NO</label><select id="new-factura-sino"><option value="">Seleccionar</option><option value="si">SI</option><option value="no">NO</option></select></div>
                <div class="form-group"><label>Copia Llave</label><input type="text" id="new-copia-llave"></div>
                <div class="form-group"><label>FED</label><input type="text" id="new-fed"></div>
                <div class="form-group"><label>Solicitud Precio</label><input type="date" id="new-fecha-sol-precio"></div>
                <div class="form-group"><label>Entrega Precio</label><input type="date" id="new-fecha-entrega-precio"></div>
                <div class="form-group"><label>Solicitud Factura CND</label><input type="date" id="new-fecha-sol-factura"></div>
                <div class="form-group"><label>Factura CND</label><input type="date" id="new-fecha-factura"></div>
                <button type="submit" class="btn-primary">Agregar</button>
                <button type="button" class="btn-secondary" onclick="cerrarModal('modalNuevo')">Cancelar</button>
            </form>
        </div>
    </div>

    <script>
let datosOriginales = [
'''

html_footer = '''];
let datosFiltrados = [];
let modalEnEdicion = null;

function calcularSLA(f1, f2) {
    if (!f1 || !f2) return 0;
    const d1 = new Date(f1);
    const d2 = new Date(f2);
    return Math.floor((d2 - d1) / (1000 * 60 * 60 * 24));
}

function poblarFiltroMarcas() {
    const marcas = [...new Set(datosOriginales.map(d => d.Marca))].sort();
    const sel1 = document.getElementById("filtro-marca");
    const sel2 = document.getElementById("new-marca");
    marcas.forEach(m => {
        const opt1 = document.createElement("option");
        opt1.value = m; opt1.textContent = m;
        sel1.appendChild(opt1);
        const opt2 = document.createElement("option");
        opt2.value = m; opt2.textContent = m;
        sel2.appendChild(opt2);
    });
}

function mostrarResumen() {
    const t = datosOriginales.length;
    const g = datosOriginales.filter(d => d["Confirmación Genessis"] === "Ok").length;
    const l = datosOriginales.filter(d => d["Copia llave"]).length;
    const f = datosOriginales.filter(d => d.FED).length;
    const fc = datosOriginales.filter(d => d["Fecha Factura CND"]).length;
    document.getElementById("resumen-grid").innerHTML = `
        <div class="card-stat"><h3>Total</h3><div class="valor">${t}</div></div>
        <div class="card-stat"><h3>Genesis OK</h3><div class="valor">${g}</div></div>
        <div class="card-stat"><h3>Sin Copia</h3><div class="valor">${t-l}</div></div>
        <div class="card-stat"><h3>Sin FED</h3><div class="valor">${t-f}</div></div>
        <div class="card-stat"><h3>Con Factura</h3><div class="valor">${fc}</div></div>
    `;
    const sl = t - l, sf = t - f;
    document.getElementById("alertas-section").innerHTML = `<h3>Alertas</h3>
        ${sl > 0 ? "<div style='padding: 10px; background: #fff3e0; margin: 5px 0;'><strong>" + sl + "</strong> sin copia de llave</div>" : ""}
        ${sf > 0 ? "<div style='padding: 10px; background: #fff3e0; margin: 5px 0;'><strong>" + sf + "</strong> sin FED</div>" : ""}
        ${sl === 0 && sf === 0 ? "<div style='color: green; font-weight: bold;'>Todo en orden</div>" : ""}
    `;
}

function mostrarTabla() {
    const tb = document.getElementById("tabla-body");
    tb.innerHTML = "";
    datosFiltrados.forEach(v => {
        const s1 = calcularSLA(v["Fecha Solicitud Precio"], v["Fecha Entrega Precio"]);
        const s2 = calcularSLA(v["Fecha Entrega Precio"], v["Fecha Solicitud Factura CND"]);
        const s3 = calcularSLA(v["Fecha Solicitud Factura CND"], v["Fecha Factura CND"]);
        const tr = document.createElement("tr");
        tr.innerHTML = `<td><button class="btn-primary" onclick="abrirModalEditar('${v.Patente}')" style="padding: 5px 10px; font-size: 0.8em;">Editar</button></td>
            <td>${v.Patente}</td><td>${v.Marca}</td><td><strong>${v.Gerencia}</strong></td><td>${v.Modelo.substring(0, 25)}</td>
            <td>${v.Categoria}</td><td>${v["Fecha Entrega a CPD"]}</td><td>${v["Numero Factura"] || "-"}</td><td>${v["Copia llave"] ? "✓" : ""}</td>
            <td>${v.FED ? "✓" : ""}</td><td>${v["Confirmación Genessis"] === "Ok" ? "✓" : ""}</td>
            <td>${v["Fecha Solicitud Precio"] || "-"}</td><td>${v["Fecha Entrega Precio"] || "-"}</td>
            <td>${v["Fecha Solicitud Factura CND"] || "-"}</td><td>${v["Fecha Factura CND"] || "-"}</td>
            <td style="background: ${s1 > 0 ? "#e8f5e9" : "#fff"}; text-align: center;"><div style="font-size: 1.1em;">📅</div><strong>${s1 > 0 ? s1 + " d" : "-"}</strong><div style="font-size: 0.7em; color: #666;">Solicitud</div></td>
            <td style="background: ${s2 > 0 ? "#fff3e0" : "#fff"}; text-align: center;"><div style="font-size: 1.1em;">⏰</div><strong>${s2 > 0 ? s2 + " d" : "-"}</strong><div style="font-size: 0.7em; color: #666;">Entrega</div></td>
            <td style="background: ${s3 > 0 ? "#e3f2fd" : "#fff"}; text-align: center;"><div style="font-size: 1.1em;">📬</div><strong>${s3 > 0 ? s3 + " d" : "-"}</strong><div style="font-size: 0.7em; color: #666;">Factura</div></td>`;
        tb.appendChild(tr);
    });
}

function inicializar() {
    mostrarResumen();
}

function aplicarFiltros() {
    const m = document.getElementById("filtro-marca").value;
    const g = document.getElementById("filtro-gerencia").value;
    const c = document.getElementById("filtro-categoria").value;
    const fe = document.getElementById("filtro-fecha-entrega").value;
    const l = document.getElementById("filtro-llave").value;
    const f = document.getElementById("filtro-fed").value;
    const gen = document.getElementById("filtro-genesis").value;
    const b = document.getElementById("filtro-busqueda").value.toUpperCase();

    datosFiltrados = datosOriginales.filter(v => {
        const tieneFechaEntrega = !fe || v["Fecha Entrega a CPD"] >= fe;
        const tieneL = l === "" || (l === "si" && v["Copia llave"]) || (l === "no" && !v["Copia llave"]);
        const tieneF = f === "" || (f === "si" && v.FED) || (f === "no" && !v.FED);
        const tieneGen = gen === "" || (gen === "Ok" && v["Confirmación Genessis"] === "Ok") || (gen === "Sin" && !v["Confirmación Genessis"]);
        const cumpleBusqueda = !b || v.Patente.includes(b) || v.VIN.includes(b);

        return (!m || v.Marca === m) && (!g || v.Gerencia === g) && (!c || v.Categoria === c) &&
               tieneFechaEntrega && tieneL && tieneF && tieneGen && cumpleBusqueda;
    });
    mostrarTabla();
}

function limpiarFiltros() {
    document.getElementById("filtro-marca").value = "";
    document.getElementById("filtro-gerencia").value = "";
    document.getElementById("filtro-categoria").value = "";
    document.getElementById("filtro-busqueda").value = "";
    datosFiltrados = [...datosOriginales];
    mostrarTabla();
}

function abrirModalEditar(p) {
    const v = datosOriginales.find(x => x.Patente === p);
    if (!v) return;
    modalEnEdicion = p;
    document.getElementById("edit-patente").value = v.Patente;
    document.getElementById("edit-numero-factura").value = v["Numero Factura"] || "";
    document.getElementById("edit-factura-sino").value = v["Fecha Factura CND"] ? "si" : "no";
    document.getElementById("edit-copia-llave").value = v["Copia llave"] || "";
    document.getElementById("edit-fed").value = v.FED || "";
    document.getElementById("edit-genesis").value = v["Confirmación Genessis"] || "";
    document.getElementById("edit-fecha-sol-precio").value = v["Fecha Solicitud Precio"] || "";
    document.getElementById("edit-fecha-entrega-precio").value = v["Fecha Entrega Precio"] || "";
    document.getElementById("edit-fecha-sol-factura").value = v["Fecha Solicitud Factura CND"] || "";
    document.getElementById("edit-fecha-factura").value = v["Fecha Factura CND"] || "";
    document.getElementById("modalEditar").classList.add("show");
}

function abrirModalNuevo() {
    document.getElementById("formNuevo").reset();
    document.getElementById("modalNuevo").classList.add("show");
}

function cerrarModal(m) {
    document.getElementById(m).classList.remove("show");
    modalEnEdicion = null;
}

function guardarEdicion(e) {
    e.preventDefault();
    const v = datosOriginales.find(x => x.Patente === modalEnEdicion);
    if (!v) return;
    v["Numero Factura"] = document.getElementById("edit-numero-factura").value;
    const facturaSino = document.getElementById("edit-factura-sino").value;
    if (facturaSino === "si" && !v["Fecha Factura CND"]) {
        const hoy = new Date().toISOString().split('T')[0];
        v["Fecha Factura CND"] = hoy;
    } else if (facturaSino === "no") {
        v["Fecha Factura CND"] = "";
    }
    v["Copia llave"] = document.getElementById("edit-copia-llave").value;
    v.FED = document.getElementById("edit-fed").value;
    v["Confirmación Genessis"] = document.getElementById("edit-genesis").value;
    v["Fecha Solicitud Precio"] = document.getElementById("edit-fecha-sol-precio").value;
    v["Fecha Entrega Precio"] = document.getElementById("edit-fecha-entrega-precio").value;
    v["Fecha Solicitud Factura CND"] = document.getElementById("edit-fecha-sol-factura").value;
    v["Fecha Factura CND"] = document.getElementById("edit-fecha-factura").value;
    guardarEnLocalStorage();
    cerrarModal("modalEditar");
    mostrarTabla();
    mostrarResumen();
}

function getGerencia(m) {
    const dc = ["KIA", "SUBARU", "DFSK", "DONGFENG", "SINOTRUK"];
    const nb = ["OPEL", "PEUGEOT", "CITROEN", "NISSAN", "GEELY", "LEAD MOTORS", "MG", "LYNK & CO"];
    const mu = m.toUpperCase();
    return dc.some(d => mu.includes(d)) ? "DC" : nb.some(n => mu.includes(n)) ? "NB" : "SIN ASIGNAR";
}

function agregarVehiculo(e) {
    e.preventDefault();
    const p = document.getElementById("new-patente").value;
    if (datosOriginales.find(x => x.Patente === p)) {
        alert("Ya existe");
        return;
    }
    const m = document.getElementById("new-marca").value;
    datosOriginales.push({
        Marca: m, Modelo: document.getElementById("new-modelo").value, Patente: p,
        VIN: document.getElementById("new-vin").value, Responsable: "NUEVO", Sucursal: "PENDIENTE",
        "Fecha Entrega a CPD": document.getElementById("new-fecha-entrega").value,
        "Numero Factura": document.getElementById("new-numero-factura").value,
        "Fecha Factura CND": document.getElementById("new-factura-sino").value === "si" ? new Date().toISOString().split('T')[0] : "",
        "Copia llave": document.getElementById("new-copia-llave").value, FED: document.getElementById("new-fed").value,
        "Confirmación Genessis": "", Comentarios: "", Documentos: "", Precompra: "",
        Categoria: document.getElementById("new-categoria").value, "Solicitud Precio Toma": "",
        "Solicitud Factura": "", "Fecha Solicitud Precio Toma": "",
        "Fecha Solicitud Factura": "", "Fecha Factura": "", SLA_Dias: 0, Gerencia: getGerencia(m),
        "Fecha Solicitud Precio": document.getElementById("new-fecha-sol-precio").value,
        "Fecha Entrega Precio": document.getElementById("new-fecha-entrega-precio").value,
        "Fecha Solicitud Factura CND": document.getElementById("new-fecha-sol-factura").value,
        "Fecha Factura CND": document.getElementById("new-fecha-factura").value,
        SLA_Precio_Dias: 0, SLA_Factura_Dias: 0, SLA_Pago_Dias: 0
    });
    guardarEnLocalStorage();
    cerrarModal("modalNuevo");
    limpiarFiltros();
    mostrarResumen();
    mostrarTabla();
}

function guardarEnLocalStorage() {
    localStorage.setItem("cpd-datos", JSON.stringify(datosOriginales));
}

function cargarDelLocalStorage() {
    const g = localStorage.getItem("cpd-datos");
    if (g) {
        try {
            datosOriginales = JSON.parse(g);
            datosFiltrados = [...datosOriginales];
        } catch (e) {
            datosFiltrados = [...datosOriginales];
        }
    } else {
        datosFiltrados = [...datosOriginales];
    }
}

cargarDelLocalStorage();
inicializar();
poblarFiltroMarcas();
mostrarTabla();
    </script>
</body>
</html>
'''

# Generar HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_header)
    # Escribir datos en múltiples líneas
    for i, registro in enumerate(datos):
        json_str = json.dumps(registro, ensure_ascii=False)
        f.write(json_str)
        if i < len(datos) - 1:
            f.write(',\n')
        else:
            f.write('\n')
    f.write(html_footer)

print(f"HTML generado - {len(datos)} registros embebidos")
