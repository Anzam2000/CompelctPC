def get_best_component_by_price(db_path, component_type, max_price):
    """
    Возвращает комплектующий с максимальным баллом, цена которого не превышает max_price
    
    Args:
        db_path (str): путь к файлу базы данных SQLite
        component_type (str): тип комплектующего (например, 'CPU', 'GPU', 'RAM')
        max_price (float): максимальная допустимая цена
    
    Returns:
        dict: информация о комплектующем или None если не найдено
    """
    try:
        # Подключаемся к базе данных
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row  # Для доступа к колонкам по имени
        
        cursor = conn.cursor()
        
        # SQL запрос для поиска комплектующего с максимальным баллом в рамках цены
        query = """
        SELECT * FROM components 
        WHERE type = ? AND price <= ? 
        ORDER BY score DESC, price ASC 
        LIMIT 1
        """
        
        cursor.execute(query, (component_type, max_price))
        result = cursor.fetchone()
        
        conn.close()
        
        if result:
            return dict(result)  # Преобразуем в словарь для удобства
        else:
            return None
            
    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        return None
