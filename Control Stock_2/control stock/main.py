import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from datetime import datetime

st.set_page_config(
    page_title="Control de Comercio",
    page_icon="🧻",
)


selected = option_menu(
    menu_title='Menu Principal',
    options=['Home', 'Productos', 'Proveedores', 'Clientes','Ventas', 'Egresos'],
    menu_icon='gear',
    icons=['house', 'bi-basket-fill', 'bi-truck', ' bi-person-fill', 'bi-currency-dollar', 'bi-cash-stack'],
    default_index=0,
    orientation='horizontal',
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "18px"}, 
        "nav-link": {"font-size": "18px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "lightblue"},
    }
)

####################################################################################################

if selected == 'Home':
    st.title("Bienvenido Alfred! 👋")
    st.write()
    st.markdown(
        """
        Esta aplicación te ayudará a hacer un seguimiento detallado de tu negocio, permitiéndote mantener un control efectivo sobre el mismo.

        
        ### Como Ingresar?!
        **👆 Selecciona en el Menu Principal que se encuentra el la parte superior de la pagina** la opción que desees explorar:
        
        
        ### Que encontraras en cada opcion
        En cada sección tendrás la capacidad de agregar, modificar y analizar los datos ingresados.

        **Productos:** Aquí encontrarás información relevante sobre tus productos, incluyendo cantidad disponible, precios y más.

        **Proveedores:** Detalles como número de teléfono, dirección y contacto para mantener una comunicación efectiva con tus proveedores.

        **Clientes:** Información detallada sobre tus clientes, incluyendo su información de contacto y ubicación para mejorar las relaciones comerciales.

        **Egresos:** Detalles completos de cada gasto realizado en tu negocio, proporcionando una visión clara de tus costos operativos.

        **Ventas:** Información detallada sobre las ventas realizadas, incluyendo cantidad vendida, cliente asociado y más para un análisis exhaustivo de tus operaciones comerciales.
    """
    )

   
# Obtener la fecha actual en español
meses = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
]

dias_semana = [
    "lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"
]

now = datetime.now()
current_date = f"{dias_semana[now.weekday()]}, {now.day} de {meses[now.month - 1]} de {now.year}"

# Mostrar la barra lateral con la fecha actual
st.sidebar.title(f'📅Fecha:')
st.sidebar.markdown(
    f'<h1 style="color: #333;">{current_date}</h1>',
    unsafe_allow_html=True
)


    
#############################################################################################    
    
if selected == 'Productos':
    st.title(f'Productos') 
    st.markdown("""
                En esta Pagina se muestra una tabla con los datos de los productos existentes, la cual la podra observar abajo.\n
                ***👈Podes ingresar en la barra lateral***, para agregar nuevos prductos o modificar los que ya existen. 
                Seleccione la accion que desea realizar en la Barra desplegable de 'Gestion de productos.'\n
                En la barra lateral podes agregregar o modificar Nombre del producto, Cantidad, Precio de compra y Preciode venta,
                Una vez que rellenas los campos oprima el boton 'Agregar'.""")
                
    st.header(f'Tabla de Productos')
    # Función para cargar el DataFrame desde un archivo CSV
    def cargar_df():
        try:
            df = pd.read_csv("Productos.csv")
        except FileNotFoundError:
            df = pd.DataFrame(columns=['Nombre_Producto', 'Cantidad', 'Precio_Compra', 'Precio_Venta'])
        return df

    # Función para guardar el DataFrame en un archivo CSV
    def guardar_df(df):
        df.to_csv("Productos.csv", index=False)

    # Cargar el DataFrame al inicio de la aplicación
    df = cargar_df()

    # Mostrar el DataFrame actualizado
    st.dataframe(df)

    # Variables para rastrear la acción
    accion_realizada = None
    indice_modificado = None

    # Sidebar
    # Título grande para la selección de gestión de productos
    st.sidebar.title("Gestión de Productos")

    # Opciones de la selección de gestión de productos
    accion = st.sidebar.selectbox("Seleccione una acción", ["Agregar Nuevo Producto", "Modificar Producto"])
    
    
    
    if accion == "Agregar Nuevo Producto":
        st.sidebar.title("Agregar Nuevo Producto")
        Nombre_Producto = st.sidebar.text_input('Nombre_Producto:')
        Cantidad = st.sidebar.number_input('Cantidad:', min_value=0, step=1)
        Precio_Compra = st.sidebar.number_input('Precio_Compra:', min_value=0.0)
        Precio_Venta = st.sidebar.number_input('Precio_Venta:', min_value=0.0)
        fecha_actual = datetime.now()
        fecha_str = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
        
        if st.sidebar.button("Agregar"):
            # Cargar el DataFrame existente
            df = cargar_df()

            if Nombre_Producto is None:
                st.sidebar.warning("Debe ingresar el nombre del producto.")
            elif Nombre_Producto.lower() in df['Nombre_Producto'].str.lower().values:
                st.sidebar.warning("El producto ya existe. Por favor, elige otro nombre.")
            else:
                # Crear nueva fila con los datos del nuevo producto
                nueva_fila = pd.DataFrame({'Nombre_Producto': [Nombre_Producto],
                                        'Cantidad': [Cantidad],
                                        'Precio_Compra': [Precio_Compra],
                                        'Precio_Venta': [Precio_Venta],
                                        'Fecha': [fecha_str]})
                
                # Concatenar el DataFrame original con el nuevo DataFrame
                df = pd.concat([df, nueva_fila], ignore_index=True)

                # Guardar el DataFrame actualizado
                guardar_df(df)
                accion_realizada = "Agregado"
                indice_modificado = df.shape[0] - 1  # Í

    elif accion == "Modificar Producto":
        st.sidebar.title("Modificar Producto")
        opciones = df['Nombre_Producto'].tolist()
        producto_modificar = st.sidebar.selectbox("Selecciona un producto:", opciones)

        if producto_modificar:
            indice_modificar = df[df['Nombre_Producto'] == producto_modificar].index[0]
            Cantidad = st.sidebar.number_input('Cantidad:', min_value=0, step=1, value=df.loc[indice_modificar, 'Cantidad'])
            Precio_Compra = st.sidebar.number_input('Precio_Compra:', min_value=0.0, value=df.loc[indice_modificar, 'Precio_Compra'])
            Precio_Venta = st.sidebar.number_input('Precio_Venta:', min_value=0.0, value=df.loc[indice_modificar, 'Precio_Venta'])

            if st.sidebar.button("Modificar"):
                # Actualizar los valores en el DataFrame
                df.loc[indice_modificar, 'Cantidad'] = Cantidad
                df.loc[indice_modificar, 'Precio_Compra'] = Precio_Compra
                df.loc[indice_modificar, 'Precio_Venta'] = Precio_Venta

                # Guardar el DataFrame actualizado
                guardar_df(df)
                accion_realizada = "Modificado"
                indice_modificado = indice_modificar
    st.header("Producto agregado o modificado")
    # Mostrar la fila que se agregó o modificó
    if accion_realizada:
        st.sidebar.success(f"Se ha {accion_realizada} el producto:")
        st.dataframe(df.iloc[indice_modificado:indice_modificado+1])

############################################################################################################

   
if selected == 'Proveedores':    
    st.title(f'Proveedores') 
    st.markdown("""
                En esta Pagina se muestra una tabla con los datos de los productos existentes, la cual la podra observar abajo.\n
                ***👈Podes ingresar en la barra lateral***, para agregar nuevos prductos o modificar los que ya existen. 
                Seleccione la accion que desea realizar en la Barra desplegable de 'Gestion de productos.'\n
                En la barra lateral podes agregregar o modificar Nombre del producto, Cantidad, Precio de compra y Preciode venta,
                Una vez que rellenas los campos oprima el boton 'Agregar'.""")
                
    st.header(f'Tabla de Proveedores')
    # Función para cargar el DataFrame desde un archivo CSV
    def cargar_df():
        try:
            df = pd.read_csv("Proveedores.csv")
        except FileNotFoundError:
            df = pd.DataFrame(columns=['Nombre_Proveedor', 'Contaco', 'Telefono', 'Email', 'Direccion'])
        return df

    # Función para guardar el DataFrame en un archivo CSV
    def guardar_df(df):
        df.to_csv("Proveedores.csv", index=False)

    # Cargar el DataFrame al inicio de la aplicación
    df = cargar_df()

    # Mostrar el DataFrame actualizado
    st.dataframe(df)

    # Variables para rastrear la acción
    accion_realizada = None
    indice_modificado = None

    # Sidebar
    # Título grande para la selección de gestión de productos
    st.sidebar.title("Gestión de Proveedores")

# Opciones de la selección de gestión de productos
    accion = st.sidebar.selectbox("Seleccione una acción", ["Agregar Nuevo Proveedores", "Modificar Proveedores"])
    
    
    
    if accion == "Agregar Nuevo Proveedores":
        st.sidebar.title("Agregar Nuevo Proveedores")
        Nombre_Proveedor = st.sidebar.text_input('Nombre_Proveedor:')
        Contacto = st.sidebar.text_input('Contacto:')
        Telefono = st.sidebar.text_input('Telefono:')
        Email = st.sidebar.text_input('Email:')
        Direccion = st.sidebar.text_input('Direccion:')
        fecha_actual = datetime.now()
        fecha_str = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
        
        if st.sidebar.button("Agregar"):
            # Cargar el DataFrame existente
            df = cargar_df()

            if Nombre_Proveedor is None:
                st.sidebar.warning("Debe ingresar el nombre del Proveedores.")
            elif Nombre_Proveedor.lower() in df['Nombre_Proveedor'].str.lower().values:
                st.sidebar.warning("El Proveedor ya existe. Por favor, elige otro nombre.")
            else:
                # Crear nueva fila con los datos del nuevo Proveedores
                nueva_fila = pd.DataFrame({'Nombre_Proveedor': [Nombre_Proveedor],
                                        'Contacto': [Contacto],
                                        'Telefono': [Telefono],
                                        'Email': [Email],
                                        'Direccion': [Direccion],
                                        'Fecha': [fecha_str]})
                
                # Concatenar el DataFrame original con el nuevo DataFrame
                df = pd.concat([df, nueva_fila], ignore_index=True)

                # Guardar el DataFrame actualizado
                guardar_df(df)
                accion_realizada = "Agregado"
                indice_modificado = df.shape[0] - 1  # Índice de la fila recién agregada

    elif accion == "Modificar Proveedor":
        st.sidebar.title("Modificar Proveedor")
        opciones = df['Nombre_Proveedor'].tolist()
        Proveedor_modificar = st.sidebar.selectbox("Selecciona un Proveedor:", opciones)

        if Proveedor_modificar:
            indice_modificar = df[df['Nombre_Proveedor'] == Proveedor_modificar].index[0]
            Telefono = st.sidebar.text_input('Telefono:', value=df.loc[indice_modificar, 'Telefono'])
            Contacto = st.sidebar.text_input('Contacto:', value=df.loc[indice_modificar, 'Contacto'])
            Email = st.sidebar.text_input('Email:', value=df.loc[indice_modificar, 'Email'])
            Direccion = st.sidebar.text_input('Direccion:', value=df.loc[indice_modificar, 'Direccion'])
        
        if st.sidebar.button("Modificar"):
            # Actualizar los valores en el DataFrame
            df.loc[indice_modificar, 'Telefono'] = Telefono
            df.loc[indice_modificar, 'Contacto'] = Contacto
            df.loc[indice_modificar, 'Email'] = Email
            df.loc[indice_modificar, 'Direccion'] = Direccion

            # Guardar el DataFrame actualizado
            guardar_df(df)
            accion_realizada = "Modificado"
            indice_modificado = indice_modificar
                
    st.header("Proveedor agregado o modificado")
    # Mostrar la fila que se agregó o modificó
    if accion_realizada:
        st.sidebar.success(f"Se ha {accion_realizada} el Proveedor:")
        st.dataframe(df.iloc[indice_modificado:indice_modificado+1])    
    
    
    
############################################################################    
    
    
    
if selected == 'Clientes':    
    st.title(f'Clientes') 
    st.markdown("""
                En esta Pagina se muestra una tabla con los datos de los productos existentes, la cual la podra observar abajo.\n
                ***👈Podes ingresar en la barra lateral***, para agregar nuevos prductos o modificar los que ya existen. 
                Seleccione la accion que desea realizar en la Barra desplegable de 'Gestion de productos.'\n
                En la barra lateral podes agregregar o modificar Nombre del producto, Cantidad, Precio de compra y Preciode venta,
                Una vez que rellenas los campos oprima el boton 'Agregar'.""")
                
    st.header(f'Tabla de Clientes')
    # Función para cargar el DataFrame desde un archivo CSV
    def cargar_df():
        try:
            df = pd.read_csv("Clientes.csv")
        except FileNotFoundError:
            df = pd.DataFrame(columns=['Nombre_Cliente', 'Contaco', 'Telefono', 'Email', 'Direccion'])
        return df

    # Función para guardar el DataFrame en un archivo CSV
    def guardar_df(df):
        df.to_csv("Clientes.csv", index=False)

    # Cargar el DataFrame al inicio de la aplicación
    df = cargar_df()

    # Mostrar el DataFrame actualizado
    st.dataframe(df)

    # Variables para rastrear la acción
    accion_realizada = None
    indice_modificado = None

    # Sidebar
    # Título grande para la selección de gestión de Clientes
    st.sidebar.title("Gestión de Clientes")

    # Opciones de la selección de gestión de Clientes
    accion = st.sidebar.selectbox("Seleccione una acción", ["Agregar Nuevo Cliente", "Modificar Cliente"])
    
    
    
    if accion == "Agregar Nuevo Cliente":
        st.sidebar.title("Agregar Nuevo Cliente")
        Nombre_Cliente = st.sidebar.text_input('Nombre_Cliente:')
        Contacto = st.sidebar.text_input('Contacto:')
        Telefono = st.sidebar.text_input('Telefono:')
        Email = st.sidebar.text_input('Email:')
        Direccion = st.sidebar.text_input('Direccion:')
        fecha_actual = datetime.now()
        fecha_str = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
        
        if st.sidebar.button("Agregar"):
            # Cargar el DataFrame existente
            df = cargar_df()

            if Nombre_Cliente is None:
                st.sidebar.warning("Debe ingresar el nombre del Cliente.")
            elif Nombre_Cliente.lower() in df['Nombre_Cliente'].str.lower().values:
                st.sidebar.warning("El Cliente ya existe. Por favor, elige otro nombre.")
            else:
                # Crear nueva fila con los datos del nuevo Cliente
                nueva_fila = pd.DataFrame({'Nombre_Cliente': [Nombre_Cliente],
                                        'Contacto': [Contacto],
                                        'Telefono': [Telefono],
                                        'Email': [Email],
                                        'Direccion': [Direccion],
                                        'Fecha': [fecha_str]})
                
                # Concatenar el DataFrame original con el nuevo DataFrame
                df = pd.concat([df, nueva_fila], ignore_index=True)

                # Guardar el DataFrame actualizado
                guardar_df(df)
                accion_realizada = "Agregado"
                indice_modificado = df.shape[0] - 1  # Índice de la fila recién agregada

    elif accion == "Modificar Cliente":
        st.sidebar.title("Modificar Cliente")
        opciones = df['Nombre_Cliente'].tolist()
        Cliente_modificar = st.sidebar.selectbox("Selecciona un Cliente:", opciones)

        if Cliente_modificar:
            indice_modificar = df[df['Nombre_Cliente'] == Cliente_modificar].index[0]
            Telefono = st.sidebar.text_input('Telefono:', value=df.loc[indice_modificar, 'Telefono'])
            Contacto = st.sidebar.text_input('Contacto:', value=df.loc[indice_modificar, 'Contacto'])
            Email = st.sidebar.text_input('Email:', value=df.loc[indice_modificar, 'Email'])
            Direccion = st.sidebar.text_input('Direccion:', value=df.loc[indice_modificar, 'Direccion'])
        
        if st.sidebar.button("Modificar"):
            # Actualizar los valores en el DataFrame
            df.loc[indice_modificar, 'Telefono'] = Telefono
            df.loc[indice_modificar, 'Contacto'] = Contacto
            df.loc[indice_modificar, 'Email'] = Email
            df.loc[indice_modificar, 'Direccion'] = Direccion

            # Guardar el DataFrame actualizado
            guardar_df(df)
            accion_realizada = "Modificado"
            indice_modificado = indice_modificar
                
    st.header("Cliente agregado o modificado")
    # Mostrar la fila que se agregó o modificó
    
    if accion_realizada:
        st.sidebar.success(f"Se ha {accion_realizada} el Cliente:")
        st.dataframe(df.iloc[indice_modificado:indice_modificado+1])

##########################################################################

if selected == 'Ventas':    
    st.title(f'Ventas') 
    st.markdown("""
                En esta página se muestra una tabla con los datos de las ventas existentes, la cual se puede observar abajo.\n
                ***👈Puedes ingresar en la barra lateral*** para agregar nuevas ventas. 
                Una vez que completes los campos, presiona el botón 'Agregar'.""")
                
    st.header(f'Tabla de Ventas')

    # Función para cargar el DataFrame desde un archivo CSV
    def cargar_df(nombre_archivo):
        try:
            df = pd.read_csv(nombre_archivo)
        except FileNotFoundError:
            df = pd.DataFrame(columns=['Nombre_Producto', 'Cantidad', 'Precio_Venta', 'Total', 'Nombre_Cliente', 'Fecha'])
        return df

    # Función para guardar el DataFrame en un archivo CSV
    def guardar_df(df, nombre_archivo):
        df.to_csv(nombre_archivo, index=False)

    # Cargar el DataFrame de productos y clientes
    df_productos = cargar_df("Productos.csv")
    df_clientes = cargar_df("Clientes.csv")

    # Inicializar el DataFrame de ventas
    df_ventas = cargar_df("Ventas.csv")

    # Sidebar para agregar ventas
    st.sidebar.title("Agregar Venta")
    producto_elegido = st.sidebar.selectbox("Selecciona un Producto:", df_productos['Nombre_Producto'].tolist())
    cantidad = st.sidebar.number_input('Cantidad:', min_value=1, step=1)
    precio_venta = df_productos[df_productos['Nombre_Producto'] == producto_elegido]['Precio_Venta'].values[0]
    nombre_cliente = st.sidebar.selectbox("Selecciona un Cliente:", df_clientes['Nombre_Cliente'].tolist())
    fecha_actual = datetime.now()
    fecha_str = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")

    if st.sidebar.button("Agregar"):
        # Calcular el total
        total = cantidad * precio_venta

        # Crear una nueva fila con los datos de la venta
        nueva_venta = pd.DataFrame({
            'Nombre_Producto': [producto_elegido],
            'Cantidad': [cantidad],
            'Precio_Venta': [precio_venta],
            'Total': [total],
            'Nombre_Cliente': [nombre_cliente],
            'Fecha': [fecha_str]
        })

        # Concatenar el DataFrame original con la nueva venta
        df_ventas = pd.concat([df_ventas, nueva_venta], ignore_index=True)

        # Guardar el DataFrame actualizado
        guardar_df(df_ventas, "Ventas.csv")

        # Mostrar mensaje de éxito
        st.sidebar.success("Venta agregada correctamente.")

    # Mostrar el DataFrame actualizado de ventas
    st.dataframe(df_ventas)
