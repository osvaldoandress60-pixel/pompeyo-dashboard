# Panel CPD - Nómina de Entregados a CPD
## Pompeyo Carrasco

### 📋 Descripción
Dashboard interactivo profesional para la gestión de vehículos entregados a CPD con:
- ✅ Resumen ejecutivo con métricas clave
- 📊 Alertas automáticas de documentación incompleta
- 🔍 Filtros interactivos (Sucursal, Responsable, Estado Genesis)
- 📈 Tabla detallada y buscable de 429 vehículos
- 🎨 Diseño corporativo Pompeyo (azul rey, navy, celeste)

### 👥 Colaboradores Autorizados
- Genessis Diaz
- Leyla Rivas
- Fran Correa
- Jaime Arratia
- Dayubri González

### 🚀 Cómo Desplegar en Cloudflare Pages

#### Opción 1: Desde GitHub (Recomendado)
1. Sube este proyecto a tu repositorio de GitHub
2. Ve a [Cloudflare Dashboard](https://dash.cloudflare.com)
3. Selecciona **Pages** → **Create a project**
4. Conecta tu cuenta de GitHub y selecciona el repositorio
5. Configuración de compilación:
   - **Build command**: (dejar vacío)
   - **Build output directory**: `.` (directorio raíz)
6. ¡Listo! Tu panel estará disponible en `https://cpd-dashboard.pages.dev`

#### Opción 2: Despliegue Manual con Wrangler
```bash
# 1. Instala Wrangler (CLI de Cloudflare)
npm install -g wrangler

# 2. Autentica con Cloudflare
wrangler login

# 3. Despliega desde este directorio
wrangler pages deploy . --project-name=cpd-dashboard
```

#### Opción 3: Drag & Drop
1. Ve a Cloudflare Pages
2. Selecciona "Upload assets"
3. Arrastra la carpeta del proyecto
4. Espera a que se complete el upload

### 📊 Características del Dashboard

**Resumen Ejecutivo:**
- Total de vehículos
- Confirmados en Genesis
- Sin confirmar Genesis
- Sin copia de llave
- Sin FED
- Con copia de llave

**Alertas Automáticas:**
- Vehículos sin copia de llave
- Vehículos sin FED
- Vehículos sin confirmar Genesis

**Filtros Disponibles:**
- 🏢 Sucursal (TEST CAR, RENTING, MOVICENTER, etc.)
- 👤 Responsable (Genessis, Leyla, Fran, Jaime, Dayubri, etc.)
- ✅ Confirmación Genesis (Ok, En Renting, Sin Confirmar)
- 🔎 Búsqueda libre (Patente, VIN, Marca)

### 🔐 Seguridad y Privacidad
- Panel de solo lectura (visualización de datos)
- Datos embebidos en HTML estático (sin servidor)
- Nada se almacena o transmite a terceros
- Compatible con Cloudflare Access para control de acceso adicional

### 📱 Compatibilidad
- ✅ Desktop (Chrome, Firefox, Safari, Edge)
- ✅ Tablet (iPad, tablets Android)
- ✅ Mobile (responsive design)
- ✅ Impresión amigable (CSS print-ready)

### 📝 Notas Técnicas
- **Formato**: HTML5 estático + JavaScript vanilla
- **Datos**: 429 registros embebidos en el HTML
- **Tamaño**: ~300KB (optimizado)
- **Actualización**: Para actualizar datos, regenerar el archivo desde Excel

### 🎨 Colores Corporativos Pompeyo
- Azul Rey: `#003D7A`
- Navy: `#1A3A52`
- Celeste: `#0099FF`
- Sky Blue: `#00BFFF`

### 📞 Soporte
Para actualizar datos del panel, contacta con el Jefe Comercial de Post Venta.

---
**Desarrollado con ❤️ por Claude Code**
**Última actualización**: 2026-09-09
