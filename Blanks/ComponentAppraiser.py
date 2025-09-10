# ДАННЫЙ КОД ЯВЛЯЕТСЯ ЗАГОТОВКОЙ И НУЖДАЕТСЯ В ПЕРЕПРОВЕРКЕ ДЛЯ ДАЛЬНЕЙШЕГО ИСПОЛЬЗОВАНИЯ!!!

class ComponentScorer:
    def __init__(self):
        self.weights = {
            'cpu': {
                'cores': 0.25,
                'frequency': 0.20,
                'l2_cache': 0.15,
                'l3_cache': 0.15,
                'memory_channels': 0.10,
                'graphics': 0.05,
                'tdp': 0.10
            },
            'ram': {
                'total_size': 0.30,
                'memory_type': 0.20,
                'module_size': 0.10,
                'modules_count': 0.10,
                'frequency': 0.15,
                'timings': 0.10,
                'latency': 0.05
            },
            'motherboard': {
                'chipset': 0.25,
                'memory_slots': 0.15,
                'memory_type': 0.15,
                'memory_frequency': 0.15,
                'form_factor': 0.10,
                'pcie_slots': 0.10,
                'brand_compatibility': 0.10
            },
            'air_cooler': {
                'base_material': 0.20,
                'rotation_speed': 0.25,
                'noise_level': 0.20,
                'power_connector': 0.10,
                'max_tdp': 0.15,
                'fan_size': 0.10
            },
            'water_cooling': {
                'fan_size': 0.20,
                'radiator_sections': 0.25,
                'fans_count': 0.20,
                'power': 0.15,
                'max_tdp': 0.20
            },
            'gpu': {
                'memory_size': 0.25,
                'memory_type': 0.20,
                'memory_bus': 0.20,
                'frequency': 0.15,
                'pcie_version': 0.10,
                'connectors': 0.10
            }
        }

    def score_cpu(self, specs):
        """Оценка процессора"""
        score = 0
        
        # Количество ядер (0-100 баллов)
        cores_score = min(specs['cores'] * 10, 100) if specs['cores'] <= 16 else 100
        score += cores_score * self.weights['cpu']['cores']
        
        # Частота (0-100 баллов)
        freq_score = min((specs['frequency'] - 2000) / 20, 100) if specs['frequency'] <= 5000 else 100
        score += freq_score * self.weights['cpu']['frequency']
        
        # Кэш L2 (0-100 баллов)
        l2_score = min(specs['l2_cache'] * 5, 100)
        score += l2_score * self.weights['cpu']['l2_cache']
        
        # Кэш L3 (0-100 баллов)
        l3_score = min(specs['l3_cache'] * 2, 100)
        score += l3_score * self.weights['cpu']['l3_cache']
        
        # Количество каналов памяти
        channels_score = {1: 30, 2: 70, 4: 100, 8: 100}.get(specs['memory_channels'], 0)
        score += channels_score * self.weights['cpu']['memory_channels']
        
        # Графика
        graphics_score = 100 if specs['graphics'] else 0
        score += graphics_score * self.weights['cpu']['graphics']
        
        # TDP (чем меньше - тем лучше)
        tdp_score = max(0, 100 - (specs['tdp'] / 2))
        score += tdp_score * self.weights['cpu']['tdp']
        
        return round(score, 2)

    def score_ram(self, specs):
        """Оценка оперативной памяти"""
        score = 0
        
        # Общий объем (GB)
        total_size_score = min(specs['total_size'] * 2, 100)
        score += total_size_score * self.weights['ram']['total_size']
        
        # Тип памяти
        memory_type_scores = {'DDR3': 30, 'DDR4': 70, 'DDR5': 100}
        memory_type_score = memory_type_scores.get(specs['memory_type'], 0)
        score += memory_type_score * self.weights['ram']['memory_type']
        
        # Размер модуля
        module_size_score = min(specs['module_size'] * 5, 100)
        score += module_size_score * self.weights['ram']['module_size']
        
        # Количество модулей
        modules_score = min(specs['modules_count'] * 25, 100)
        score += modules_score * self.weights['ram']['modules_count']
        
        # Частота
        freq_scores = {2133: 30, 2666: 40, 3200: 60, 3600: 70, 4000: 80, 4800: 90, 5600: 100}
        freq_score = max(freq_scores.get(specs['frequency'], 0), 
                        min(specs['frequency'] / 40, 100))
        score += freq_score * self.weights['ram']['frequency']
        
        # Тайминги (чем меньше - тем лучше)
        timings_score = max(0, 100 - (specs['timings'] * 5))
        score += timings_score * self.weights['ram']['timings']
        
        # Латентность
        latency_score = max(0, 100 - (specs['latency'] * 10))
        score += latency_score * self.weights['ram']['latency']
        
        return round(score, 2)

    def score_motherboard(self, specs):
        """Оценка материнской платы"""
        score = 0
        
        # Чипсет (примерные оценки)
        chipset_scores = {
            'H610': 40,  'H670': 60, 'B660': 70, 'Z690': 85, 'Z790': 95,
            'A520': 40, 'B550': 65, 'X570': 85, 'X670': 95
        }
        chipset_score = chipset_scores.get(specs['chipset'], 50)
        score += chipset_score * self.weights['motherboard']['chipset']
        
        # Количество слотов памяти
        slots_score = min(specs['memory_slots'] * 25, 100)
        score += slots_score * self.weights['motherboard']['memory_slots']
        
        # Тип слотов памяти
        memory_type_score = 100 if specs['memory_type'] in ['DDR4', 'DDR5'] else 50
        score += memory_type_score * self.weights['motherboard']['memory_type']
        
        # Частота слотов памяти
        mem_freq_score = min(specs['memory_frequency'] / 40, 100)
        score += mem_freq_score * self.weights['motherboard']['memory_frequency']
        
        # Форм-фактор
        form_factor_scores = {'Mini-ITX': 60, 'Micro-ATX': 70, 'ATX': 85, 'E-ATX': 95}
        form_factor_score = form_factor_scores.get(specs['form_factor'], 50)
        score += form_factor_score * self.weights['motherboard']['form_factor']
        
        # Количество слотов PCI-E
        pcie_score = min(specs['pcie_slots'] * 20, 100)
        score += pcie_score * self.weights['motherboard']['pcie_slots']
        
        # Совместимость
        brand_score = 100 if specs['brand_compatibility'] in ['intel', 'amd'] else 0
        score += brand_score * self.weights['motherboard']['brand_compatibility']
        
        return round(score, 2)

    def score_air_cooler(self, specs):
        """Оценка воздушного охлаждения"""
        score = 0
        
        # Материал основания
        material_scores = {'aluminum': 60, 'copper': 85, 'copper+heatpipes': 100}
        material_score = material_scores.get(specs['base_material'].lower(), 50)
        score += material_score * self.weights['air_cooler']['base_material']
        
        # Скорость вращения (RPM)
        speed_score = min(specs['rotation_speed'] / 20, 100)
        score += speed_score * self.weights['air_cooler']['rotation_speed']
        
        # Уровень шума (dB, чем меньше - тем лучше)
        noise_score = max(0, 100 - (specs['noise_level'] * 5))
        score += noise_score * self.weights['air_cooler']['noise_level']
        
        # Разъем питания
        connector_scores = {'3pin': 60, '4pin': 85, 'PWM': 100}
        connector_score = connector_scores.get(specs['power_connector'], 50)
        score += connector_score * self.weights['air_cooler']['power_connector']
        
        # Макс TDP
        tdp_score = min(specs['max_tdp'] / 2, 100)
        score += tdp_score * self.weights['air_cooler']['max_tdp']
        
        # Размер вентилятора (mm)
        size_score = min(specs['fan_size'] / 2, 100)
        score += size_score * self.weights['air_cooler']['fan_size']
        
        return round(score, 2)

    def score_water_cooling(self, specs):
        """Оценка водяного охлаждения"""
        score = 0
        
        # Размер вентилятора
        fan_size_score = min(specs['fan_size'] / 2, 100)
        score += fan_size_score * self.weights['water_cooling']['fan_size']
        
        # Количество секций радиатора
        sections_score = min(specs['radiator_sections'] * 20, 100)
        score += sections_score * self.weights['water_cooling']['radiator_sections']
        
        # Количество вентиляторов
        fans_score = min(specs['fans_count'] * 25, 100)
        score += fans_score * self.weights['water_cooling']['fans_count']
        
        # Питание
        power_scores = {'3pin': 60, '4pin': 85, 'PWM': 100, 'SATA': 70, 'MOLEX': 50}
        power_score = power_scores.get(specs['power'], 50)
        score += power_score * self.weights['water_cooling']['power']
        
        # Макс TDP
        tdp_score = min(specs['max_tdp'] / 2, 100)
        score += tdp_score * self.weights['water_cooling']['max_tdp']
        
        return round(score, 2)

    def score_gpu(self, specs):
        """Оценка видеокарты"""
        score = 0
        
        # Объем памяти (GB)
        memory_score = min(specs['memory_size'] * 5, 100)
        score += memory_score * self.weights['gpu']['memory_size']
        
        # Тип памяти
        memory_type_scores = {'GDDR5': 40, 'GDDR6': 70, 'GDDR6X': 85, 'HBM2': 95}
        memory_type_score = memory_type_scores.get(specs['memory_type'], 50)
        score += memory_type_score * self.weights['gpu']['memory_type']
        
        # Шина памяти (bit)
        bus_score = min(specs['memory_bus'] * 1.5, 100)
        score += bus_score * self.weights['gpu']['memory_bus']
        
        # Частота (MHz)
        freq_score = min(specs['frequency'] / 20, 100)
        score += freq_score * self.weights['gpu']['frequency']
        
        # Версия PCI-E
        pcie_scores = {'3.0': 60, '4.0': 85, '5.0': 100}
        pcie_score = pcie_scores.get(specs['pcie_version'], 50)
        score += pcie_score * self.weights['gpu']['pcie_version']
        
        # Разъемы (количество)
        connectors_score = min(specs['connectors'] * 20, 100)
        score += connectors_score * self.weights['gpu']['connectors']
        
        return round(score, 2)

    def evaluate_system(self, components):
        """Оценка всей системы"""
        scores = {}
        
        if 'cpu' in components:
            scores['cpu'] = self.score_cpu(components['cpu'])
        
        if 'ram' in components:
            scores['ram'] = self.score_ram(components['ram'])
        
        if 'motherboard' in components:
            scores['motherboard'] = self.score_motherboard(components['motherboard'])
        
        if 'air_cooler' in components:
            scores['air_cooler'] = self.score_air_cooler(components['air_cooler'])
        
        if 'water_cooling' in components:
            scores['water_cooling'] = self.score_water_cooling(components['water_cooling'])
        
        if 'gpu' in components:
            scores['gpu'] = self.score_gpu(components['gpu'])
        
        # Общая оценка системы (средневзвешенная)
        total_score = sum(scores.values()) / len(scores) if scores else 0
        
        return {
            'component_scores': scores,
            'total_score': round(total_score, 2),
            'rating': self._get_rating(total_score)
        }
    
    def _get_rating(self, score):
        """Получить текстовую оценку"""
        if score >= 90: return "Отлично (A)"
        elif score >= 80: return "Очень хорошо (B)"
        elif score >= 70: return "Хорошо (C)"
        elif score >= 60: return "Удовлетворительно (D)"
        else: return "Плохо (F)"

# Пример использования
if __name__ == "__main__":
    scorer = ComponentScorer()
    
    # Пример данных компонентов
    components = {
        'cpu': {
            'cores': 8,
            'frequency': 3700,
            'l2_cache': 8,
            'l3_cache': 32,
            'memory_channels': 2,
            'graphics': True,
            'tdp': 65
        },
        'ram': {
            'total_size': 32,
            'memory_type': 'DDR4',
            'module_size': 16,
            'modules_count': 2,
            'frequency': 3200,
            'timings': 16,
            'latency': 10
        },
        'gpu': {
            'memory_size': 8,
            'memory_type': 'GDDR6',
            'memory_bus': 256,
            'frequency': 1700,
            'pcie_version': '4.0',
            'connectors': 4
        }
    }
    
    result = scorer.evaluate_system(components)
    print("Результаты оценки:")
    for component, score in result['component_scores'].items():
        print(f"{component.upper()}: {score} баллов")
    
    print(f"\nОбщая оценка системы: {result['total_score']} - {result['rating']}")
