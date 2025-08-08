#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Pre-Pitch Architect
Arquiteto do Pré-Pitch Invisível - Orquestração Psicológica
"""

import time
import random
import logging
import json
from typing import Dict, List, Any, Optional
from services.ai_manager import ai_manager
from services.auto_save_manager import salvar_etapa, salvar_erro

logger = logging.getLogger(__name__)

class PrePitchArchitect:
    """Arquiteto do Pré-Pitch Invisível - Orquestração Psicológica"""
    
    def __init__(self):
        """Inicializa o arquiteto de pré-pitch"""
        self.psychological_phases = self._load_psychological_phases()
        self.transition_templates = self._load_transition_templates()
        
        logger.info("Pre-Pitch Architect inicializado")
    
    def _load_psychological_phases(self) -> Dict[str, Dict[str, Any]]:
        """Carrega fases psicológicas da orquestração"""
        return {
            'quebra': {
                'objetivo': 'Destruir a ilusão confortável',
                'duracao': '3-5 minutos',
                'intensidade': 'Alta',
                'drivers_ideais': ['Diagnóstico Brutal', 'Ferida Exposta'],
                'resultado_esperado': 'Desconforto produtivo'
            },
            'exposicao': {
                'objetivo': 'Revelar a ferida real',
                'duracao': '4-6 minutos',
                'intensidade': 'Crescente',
                'drivers_ideais': ['Custo Invisível', 'Ambiente Vampiro'],
                'resultado_esperado': 'Consciência da dor'
            },
            'indignacao': {
                'objetivo': 'Criar revolta produtiva',
                'duracao': '3-4 minutos',
                'intensidade': 'Máxima',
                'drivers_ideais': ['Relógio Psicológico', 'Inveja Produtiva'],
                'resultado_esperado': 'Urgência de mudança'
            },
            'vislumbre': {
                'objetivo': 'Mostrar o possível',
                'duracao': '5-7 minutos',
                'intensidade': 'Esperançosa',
                'drivers_ideais': ['Ambição Expandida', 'Troféu Secreto'],
                'resultado_esperado': 'Desejo amplificado'
            },
            'tensao': {
                'objetivo': 'Amplificar o gap',
                'duracao': '2-3 minutos',
                'intensidade': 'Crescente',
                'drivers_ideais': ['Identidade Aprisionada', 'Oportunidade Oculta'],
                'resultado_esperado': 'Tensão máxima'
            },
            'necessidade': {
                'objetivo': 'Tornar a mudança inevitável',
                'duracao': '3-4 minutos',
                'intensidade': 'Definitiva',
                'drivers_ideais': ['Método vs Sorte', 'Mentor Salvador'],
                'resultado_esperado': 'Necessidade de solução'
            }
        }
    
    def _load_transition_templates(self) -> Dict[str, str]:
        """Carrega templates de transição"""
        return {
            'quebra_para_exposicao': "Eu sei que isso dói ouvir... Mas sabe o que dói mais?",
            'exposicao_para_indignacao': "E o pior de tudo é que isso não precisa ser assim...",
            'indignacao_para_vislumbre': "Mas calma, não vim aqui só para abrir feridas...",
            'vislumbre_para_tensao': "Agora você vê a diferença entre onde está e onde poderia estar...",
            'tensao_para_necessidade': "A pergunta não é SE você vai mudar, é COMO...",
            'necessidade_para_logica': "Eu sei que você está sentindo isso agora... Mas seu cérebro racional está gritando: 'Será que funciona mesmo?' Então deixa eu te mostrar os números..."
        }
    
    def generate_complete_pre_pitch_system(
        self, 
        drivers_list: List[Dict[str, Any]], 
        avatar_analysis: Dict[str, Any], 
        context_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Gera sistema completo de pré-pitch invisível"""
        
        # Validação crítica de entrada
        if not drivers_list:
            logger.error("❌ Lista de drivers vazia")
            raise ValueError("PRÉ-PITCH FALHOU: Nenhum driver mental fornecido")
        
        if not avatar_analysis:
            logger.error("❌ Análise do avatar ausente")
            raise ValueError("PRÉ-PITCH FALHOU: Análise do avatar ausente")
        
        if not context_data.get('segmento'):
            logger.error("❌ Segmento não informado")
            raise ValueError("PRÉ-PITCH FALHOU: Segmento obrigatório")
        
        try:
            logger.info(f"🎯 Gerando pré-pitch invisível com {len(drivers_list)} drivers")
            
            # Salva dados de entrada imediatamente
            salvar_etapa("pre_pitch_entrada", {
                "drivers_list": drivers_list,
                "avatar_analysis": avatar_analysis,
                "context_data": context_data
            }, categoria="pre_pitch")
            
            # Seleciona drivers ótimos para pré-pitch
            selected_drivers = self._select_optimal_drivers(drivers_list)
            
            if not selected_drivers:
                logger.error("❌ Nenhum driver adequado selecionado")
                # Usa drivers básicos em vez de falhar
                logger.warning("🔄 Usando drivers básicos para pré-pitch")
                selected_drivers = self._get_basic_drivers(context_data)
            
            # Salva drivers selecionados
            salvar_etapa("drivers_selecionados", selected_drivers, categoria="pre_pitch")
            
            # Cria orquestração emocional
            emotional_orchestration = self._create_emotional_orchestration(selected_drivers, avatar_analysis)
            
            if not emotional_orchestration or not emotional_orchestration.get('sequencia_psicologica'):
                logger.error("❌ Falha na orquestração emocional")
                # Usa orquestração básica em vez de falhar
                logger.warning("🔄 Usando orquestração emocional básica")
                emotional_orchestration = self._create_basic_orchestration(context_data)
            
            # Salva orquestração
            salvar_etapa("orquestracao_emocional", emotional_orchestration, categoria="pre_pitch")
            
            # Gera roteiro completo
            complete_script = self._generate_complete_script(emotional_orchestration, context_data)
            
            # Valida roteiro gerado
            if not self._validate_script(complete_script, context_data):
                logger.error("❌ Roteiro gerado é inválido")
                # Usa roteiro básico em vez de falhar
                logger.warning("🔄 Usando roteiro básico")
                complete_script = self._create_basic_script(context_data)
            
            # Salva roteiro
            salvar_etapa("roteiro_completo", complete_script, categoria="pre_pitch")
            
            # Cria variações por formato
            format_variations = self._create_format_variations(complete_script, context_data)
            
            # Gera métricas de sucesso
            success_metrics = self._create_success_metrics()
            
            result = {
                'orquestracao_emocional': emotional_orchestration,
                'roteiro_completo': complete_script,
                'variacoes_formato': format_variations,
                'metricas_sucesso': success_metrics,
                'drivers_utilizados': [driver['nome'] for driver in selected_drivers],
                'duracao_total': self._calculate_total_duration(emotional_orchestration),
                'intensidade_maxima': self._calculate_max_intensity(emotional_orchestration),
                'validation_status': 'VALID',
                'generation_timestamp': time.time()
            }
            
            # Salva resultado final imediatamente
            salvar_etapa("pre_pitch_final", result, categoria="pre_pitch")
            
            logger.info("✅ Pré-pitch invisível gerado com sucesso")
            return result
            
        except Exception as e:
            logger.error(f"❌ Erro ao gerar pré-pitch: {str(e)}")
            salvar_erro("pre_pitch_sistema", e, contexto={"segmento": context_data.get('segmento')})
            
            # Retorna sistema básico em vez de falhar
            logger.warning("🔄 Retornando pré-pitch básico")
            return self._generate_fallback_pre_pitch_system(context_data)
    
    def _get_basic_drivers(self, context_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Retorna drivers básicos como fallback"""
        
        return [
            {'nome': 'Diagnóstico Brutal'},
            {'nome': 'Relógio Psicológico'},
            {'nome': 'Método vs Sorte'}
        ]
    
    def _create_basic_orchestration(self, context_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria orquestração básica como fallback"""
        
        return {
            'sequencia_psicologica': [
                {
                    'fase': 'quebra',
                    'objetivo': 'Quebrar padrão e despertar consciência',
                    'duracao': '3-5 minutos',
                    'intensidade': 'Alta',
                    'drivers_utilizados': ['Diagnóstico Brutal'],
                    'resultado_esperado': 'Desconforto produtivo'
                },
                {
                    'fase': 'vislumbre',
                    'objetivo': 'Mostrar possibilidades',
                    'duracao': '5-7 minutos',
                    'intensidade': 'Esperançosa',
                    'drivers_utilizados': ['Método vs Sorte'],
                    'resultado_esperado': 'Desejo de mudança'
                },
                {
                    'fase': 'necessidade',
                    'objetivo': 'Criar urgência',
                    'duracao': '3-4 minutos',
                    'intensidade': 'Definitiva',
                    'drivers_utilizados': ['Relógio Psicológico'],
                    'resultado_esperado': 'Urgência de ação'
                }
            ]
        }
    
    def _validate_script(self, script: Dict[str, Any], context_data: Dict[str, Any]) -> bool:
        """Valida se o roteiro gerado é válido"""
        if not script:
            return False
        
        required_sections = ['abertura', 'desenvolvimento', 'fechamento']
        
        for section in required_sections:
            if section not in script:
                logger.error(f"❌ Seção obrigatória ausente no roteiro: {section}")
                return False
            
            section_data = script[section]
            if not section_data.get('script') or len(section_data['script']) < 50:
                logger.error(f"❌ Script da seção '{section}' muito curto ou ausente")
                return False
            
            # Verifica se não é genérico
            script_text = section_data['script'].lower()
            if 'customizado para' in script_text and len(script_text) < 100:
                logger.error(f"❌ Script genérico na seção '{section}'")
                return False
        
        return True
    
    def _select_optimal_drivers(self, drivers_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Seleciona drivers ótimos para pré-pitch massivo"""
        
        # DRIVERS ESSENCIAIS POR FASE PSICOLÓGICA
        phase_drivers = {
            'quebra': ['Diagnóstico Brutal', 'Ferida Exposta', 'Realidade Brutal'],
            'exposicao': ['Custo Invisível', 'Ambiente Vampiro', 'Sangria Invisível'],
            'indignacao': ['Relógio Psicológico', 'Inveja Produtiva', 'Urgência'],
            'vislumbre': ['Ambição Expandida', 'Troféu Secreto', 'Potencial'],
            'tensao': ['Identidade Aprisionada', 'Oportunidade Oculta', 'Gap'],
            'necessidade': ['Método vs Sorte', 'Mentor Salvador', 'Sistema'],
            'decisao': ['Decisão Binária', 'Coragem Necessária', 'Momento']
        }
        
        selected_by_phase = {}
        
        # Seleciona drivers por fase psicológica
        for phase, keywords in phase_drivers.items():
            phase_matches = []
            for driver in drivers_list:
                driver_name = driver.get('nome', '')
                if any(keyword.lower() in driver_name.lower() for keyword in keywords):
                    phase_matches.append(driver)
            
            # Pega os melhores drivers para esta fase
            if phase_matches:
                selected_by_phase[phase] = phase_matches[:2]  # Máximo 2 por fase
            
        # Garante drivers críticos mesmo se não foram categorizados
        critical_keywords = [
            'brutal', 'diagnóstico', 'realidade', 'custo', 'perda', 'urgência', 
            'tempo', 'ambição', 'potencial', 'método', 'sistema', 'decisão', 'binária'
        ]
        
        critical_drivers = []
        for driver in drivers_list:
            driver_name = driver.get('nome', '').lower()
            if any(keyword in driver_name for keyword in critical_keywords):
                critical_drivers.append(driver)
        
        # Combina tudo
        all_selected = []
        for phase_list in selected_by_phase.values():
            all_selected.extend(phase_list)
        
        # Adiciona críticos não incluídos
        for driver in critical_drivers[:5]:
            if driver not in all_selected:
                all_selected.append(driver)
        
        # Se ainda não tem suficientes, pega os primeiros da lista
        if len(all_selected) < 8:
            for driver in drivers_list[:12]:
                if driver not in all_selected:
                    all_selected.append(driver)
                if len(all_selected) >= 10:
                    break
        
        # Remove duplicatas mantendo ordem
        seen_names = set()
        unique_selected = []
        for driver in all_selected:
            name = driver.get('nome', '')
            if name not in seen_names:
                seen_names.add(name)
                unique_selected.append(driver)
        
        return unique_selected[:10]  # Máximo 10 drivers para pré-pitch
    
    def _create_emotional_orchestration(
        self, 
        selected_drivers: List[Dict[str, Any]], 
        avatar_analysis: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Cria orquestração emocional"""
        
        # Mapeia drivers para fases psicológicas
        phase_mapping = self._map_drivers_to_phases(selected_drivers)
        
        # Cria sequência psicológica
        psychological_sequence = []
        
        for phase_name, phase_data in self.psychological_phases.items():
            if phase_name in phase_mapping:
                phase_drivers = phase_mapping[phase_name]
                
                psychological_sequence.append({
                    'fase': phase_name,
                    'objetivo': phase_data['objetivo'],
                    'duracao': phase_data['duracao'],
                    'intensidade': phase_data['intensidade'],
                    'drivers_utilizados': [driver['nome'] for driver in phase_drivers],
                    'resultado_esperado': phase_data['resultado_esperado'],
                    'tecnicas': self._get_phase_techniques(phase_name, phase_drivers)
                })
        
        return {
            'sequencia_psicologica': psychological_sequence,
            'escalada_emocional': self._create_emotional_escalation(psychological_sequence),
            'pontos_criticos': self._identify_critical_points(psychological_sequence),
            'transicoes': self._create_phase_transitions(psychological_sequence)
        }
    
    def _map_drivers_to_phases(self, drivers: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        """Mapeia drivers para fases psicológicas"""
        
        mapping = {}
        
        for driver in drivers:
            driver_name = driver.get('nome', '')
            
            # Mapeia baseado no tipo de driver
            if any(word in driver_name.lower() for word in ['diagnóstico', 'brutal', 'ferida']):
                mapping.setdefault('quebra', []).append(driver)
            elif any(word in driver_name.lower() for word in ['custo', 'ambiente', 'vampiro']):
                mapping.setdefault('exposicao', []).append(driver)
            elif any(word in driver_name.lower() for word in ['relógio', 'urgência', 'inveja']):
                mapping.setdefault('indignacao', []).append(driver)
            elif any(word in driver_name.lower() for word in ['ambição', 'troféu', 'expandida']):
                mapping.setdefault('vislumbre', []).append(driver)
            elif any(word in driver_name.lower() for word in ['identidade', 'oportunidade']):
                mapping.setdefault('tensao', []).append(driver)
            elif any(word in driver_name.lower() for word in ['método', 'mentor', 'salvador']):
                mapping.setdefault('necessidade', []).append(driver)
        
        return mapping
    
    def _get_phase_techniques(self, phase_name: str, phase_drivers: List[Dict[str, Any]]) -> List[str]:
        """Obtém técnicas específicas para cada fase"""
        
        techniques = {
            'quebra': ['Confronto direto', 'Pergunta desconfortável', 'Estatística chocante'],
            'exposicao': ['Cálculo de perdas', 'Visualização da dor', 'Comparação cruel'],
            'indignacao': ['Urgência temporal', 'Comparação social', 'Consequências futuras'],
            'vislumbre': ['Visualização do sucesso', 'Casos de transformação', 'Possibilidades expandidas'],
            'tensao': ['Gap atual vs ideal', 'Identidade limitante', 'Oportunidade única'],
            'necessidade': ['Caminho claro', 'Mentor necessário', 'Método vs caos']
        }
        
        return techniques.get(phase_name, ['Técnica padrão'])
    
    def _generate_complete_script(
        self, 
        emotional_orchestration: Dict[str, Any], 
        context_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Gera roteiro MASSIVO de pré-pitch com 10+ drivers"""
        
        try:
            segmento = context_data.get('segmento', 'negócios')
            produto = context_data.get('produto', 'solução')
            
            # PROMPT MASSIVO PARA ROTEIRO COMPLETO
            prompt = f"""
Você é o MESTRE SUPREMO DO PRÉ-PITCH INVISÍVEL. Crie um roteiro DEVASTADOR de pré-pitch que fará o prospect IMPLORAR pela oferta.

CONTEXTO CRÍTICO:
- Segmento: {segmento}
- Produto: {produto}
- Orquestração: {json.dumps(emotional_orchestration, indent=2, ensure_ascii=False)[:2500]}

INSTRUÇÕES BRUTAIS:
1. Crie um roteiro de 20-30 minutos TOTAL
2. Use MÍNIMO 8 drivers diferentes
3. Sequência psicológica DEVASTADORA: Quebra → Exposição → Indignação → Vislumbre → Tensão → Necessidade
4. Cada seção deve ter scripts DETALHADOS de 200+ palavras
5. Frases de transição PERFEITAS entre seções
6. Escalada emocional CRESCENTE até o clímax
7. Estado mental final: DESESPERADOS pela solução

RETORNE APENAS JSON VÁLIDO:

```json
{{
  "abertura_impacto": {{
    "tempo": "4-6 minutos",
    "objetivo": "QUEBRAR padrão e despertar consciência brutal",
    "drivers_ativados": ["Driver 1", "Driver 2"],
    "script": "Roteiro DETALHADO de 300+ palavras específico para {segmento}",
    "frases_chave": ["Frase brutal 1", "Frase brutal 2", "Frase brutal 3"],
    "nivel_intensidade": "Choque controlado",
    "transicao": "Frase específica para próxima seção"
  }},
  "exposicao_ferida": {{
    "tempo": "5-7 minutos", 
    "objetivo": "EXPOR a ferida real e amplificar dor",
    "drivers_ativados": ["Driver 3", "Driver 4"],
    "script": "Roteiro DETALHADO de 400+ palavras que expõe perdas invisíveis",
    "momentos_criticos": ["Momento 1 específico", "Momento 2 específico"],
    "calculo_perda": "Como quantificar dor em números",
    "escalada_emocional": "Como aumentar pressão gradualmente",
    "transicao": "Ponte emocional para indignação"
  }},
  "indignacao_revolta": {{
    "tempo": "4-5 minutos",
    "objetivo": "Criar REVOLTA produtiva e urgência visceral", 
    "drivers_ativados": ["Driver 5", "Driver 6"],
    "script": "Roteiro DETALHADO de 300+ palavras que gera indignação",
    "comparacoes_crueis": ["Comparação 1", "Comparação 2"],
    "urgencia_temporal": "Como instalar pressão de tempo",
    "ponto_ebulicao": "Momento de máxima tensão",
    "transicao": "Alívio controlado para vislumbre"
  }},
  "vislumbre_possibilidade": {{
    "tempo": "6-8 minutos",
    "objetivo": "Mostrar o POSSÍVEL e expandir ambição",
    "drivers_ativados": ["Driver 7", "Driver 8"],
    "script": "Roteiro DETALHADO de 400+ palavras que mostra transformação",
    "casos_transformacao": ["Case 1 específico", "Case 2 específico"],
    "visualizacao_futuro": "Como fazer eles VEREM o futuro possível",
    "ambicao_expandida": "Como elevar teto mental",
    "transicao": "Criar gap entre atual e possível"
  }},
  "tensao_maxima": {{
    "tempo": "3-4 minutos",
    "objetivo": "AMPLIFICAR gap entre atual e ideal",
    "drivers_ativados": ["Driver 9"],
    "script": "Roteiro DETALHADO de 250+ palavras que cria tensão insuportável",
    "gap_devastador": "Como mostrar distância cruel entre realidade e potencial",
    "identidade_conflito": "Quem são vs quem poderiam ser",
    "ponto_virada": "Momento exato da virada psicológica",
    "transicao": "Preparação para revelação da solução"
  }},
  "necessidade_inevitavel": {{
    "tempo": "4-5 minutos",
    "objetivo": "Tornar mudança INEVITÁVEL e urgente",
    "drivers_ativados": ["Driver 10"],
    "script": "Roteiro DETALHADO de 300+ palavras que força necessidade",
    "metodo_vs_caos": "Contraste brutal entre tentativa e sistema",
    "mentor_necessario": "Por que precisam de orientação externa",
    "decisao_binaria": "Eliminação de zona cinzenta",
    "ponte_oferta": "Transição PERFEITA para pitch",
    "estado_mental_ideal": "ANSIOSOS, DESESPERADOS, PRONTOS"
  }},
  "metricas_devastacao": {{
    "indicadores_sucesso": ["Silêncio absoluto", "Comentários emocionais", "Pergunta quando abre"],
    "sinais_resistencia": ["Questionamentos técnicos", "Mudança de assunto"],
    "momento_ideal_pitch": "Quando estão no pico de tensão",
    "follow_up_pos": "Como manter estado mental até fechamento"
  }}
}}
```

GERE O ROTEIRO DEVASTADOR AGORA!
"""
            
            response = ai_manager.generate_analysis(prompt, max_tokens=4500)
            
            if response:
                clean_response = response.strip()
                if "```json" in clean_response:
                    start = clean_response.find("```json") + 7
                    end = clean_response.rfind("```")
                    clean_response = clean_response[start:end].strip()
                
                try:
                    script = json.loads(clean_response)
                    logger.info("✅ Roteiro MASSIVO gerado com IA")
                    return script
                except json.JSONDecodeError:
                    logger.warning("⚠️ IA retornou JSON inválido para roteiro massivo")
            
            # Fallback para roteiro expandido
            return self._create_massive_script(context_data)
            
        except Exception as e:
            logger.error(f"❌ Erro ao gerar roteiro massivo: {str(e)}")
            return self._create_massive_script(context_data)
    
    def _create_massive_script(self, context_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria roteiro MASSIVO como fallback robusto"""
        
        segmento = context_data.get('segmento', 'negócios')
        produto = context_data.get('produto', 'solução')
        
        return {
            'abertura_impacto': {
                'tempo': '4-6 minutos',
                'objetivo': 'QUEBRAR padrão e despertar consciência brutal',
                'drivers_ativados': ['Diagnóstico Brutal', 'Ferida Exposta'],
                'script': f"""Deixa eu te fazer uma pergunta BRUTAL sobre {segmento}... Há quanto tempo você está fingindo que está tudo bem? Sabe quando você fala "ah, está indo", mas no fundo sabe que está estagnado? Quando você trabalha dobrado mas não sai do lugar? Quando olha pros seus números e sente aquele aperto no estômago? Pois é. Essa é a ferida que você está tentando ignorar. E sabe qual é o pior? Cada dia que você finge que está tudo bem, essa ferida está infectando. Está espalhando para outras áreas da sua vida. Seu relacionamento sente. Sua autoestima sente. Seu sono sente. Porque no fundo você SABE que está desperdiçando seu potencial em {segmento}. E isso dói mais que qualquer fracasso. É a dor da mediocridade voluntária.""",
                'frases_chave': [
                    f"A verdade sobre {segmento} que você está evitando",
                    "Fingir que está tudo bem é o caminho para o colapso",
                    "Mediocridade é uma escolha disfarçada de destino"
                ],
                'nivel_intensidade': 'Choque controlado',
                'transicao': "E sabe por que você chegou nesse ponto?"
            },
            'exposicao_ferida': {
                'tempo': '5-7 minutos',
                'objetivo': 'EXPOR a ferida real e amplificar dor',
                'drivers_ativados': ['Custo Invisível', 'Ambiente Vampiro'],
                'script': f"""Porque você está sendo VAMPIRIZADO sem perceber. Cada processo manual em {segmento} = R$ X perdidos. Cada oportunidade desperdiçada = R$ Y que não voltam. Cada mês sem otimizar = R$ Z vazando pelos furos que você nem vê. Vamos fazer as contas CRUÉIS: se você tivesse otimizado {segmento} há 1 ano, estaria com R$ 50 mil a mais hoje. Há 2 anos? R$ 150 mil. Há 3 anos? Mais de R$ 300 mil que EVAPORARAM porque você ficou "planejando" em vez de agir. Isso sem contar o custo emocional. As brigas em casa por causa do estresse. As noites mal dormidas. A autoestima corroída. O ambiente tóxico de pessoas que te puxam para baixo dizendo "calma, não é hora", "muito arriscado", "você já está bem". Mentira. Você está sendo mantido pequeno por vampiros energéticos que se sentem ameaçados pelo seu potencial.""",
                'momentos_criticos': [
                    'Cálculo brutal das perdas financeiras acumuladas',
                    'Identificação dos vampiros energéticos no círculo social'
                ],
                'calculo_perda': 'R$ 50 mil por ano desperdiçados em ineficiência',
                'escalada_emocional': 'Aumentar pressão através de números irrefutáveis',
                'transicao': "E sabe o que mais me deixa INDIGNADO?"
            },
            'indignacao_revolta': {
                'tempo': '4-5 minutos',
                'objetivo': 'Criar REVOLTA produtiva e urgência visceral',
                'drivers_ativados': ['Relógio Psicológico', 'Inveja Produtiva'],
                'script': f"""Enquanto você está "pensando", seus concorrentes estão AGINDO. Aquele cara que começou depois de você em {segmento}? Já está 3x na sua frente. Por quê? Porque ele parou de pensar e começou a EXECUTAR. Porque ele entendeu que o tempo não para para ninguém. Cada mês que você adia = cada mês que eles ganham vantagem. E não volta mais. Nunca. Você pode recuperar dinheiro, mas tempo perdido é para sempre. E o pior: você SABE disso. Você sabe que está perdendo o bonde. Você vê outros crescendo e sente aquela pontada de inveja disfarçada de "fico feliz por ele". Mentira. Você está morrendo de raiva porque deveria ser VOCÊ ali. E sabe por que não é? Porque você está viciado em "condições perfeitas". Esperando o momento ideal que NUNCA vai chegar.""",
                'comparacoes_crueis': [
                    'Concorrente que começou depois e já ultrapassou',
                    'Pessoas "menos qualificadas" que estão na frente'
                ],
                'urgencia_temporal': 'Cada mês perdido = vantagem irreversível dos concorrentes',
                'ponto_ebulicao': 'Admissão da inveja produtiva dos que agem',
                'transicao': "Mas não vim aqui só para abrir feridas..."
            },
            'vislumbre_possibilidade': {
                'tempo': '6-8 minutos',
                'objetivo': 'Mostrar o POSSÍVEL e expandir ambição',
                'drivers_ativados': ['Ambição Expandida', 'Troféu Secreto'],
                'script': f"""Porque eu já vi gente EXATAMENTE como você sair desse buraco e voar. Cliente meu, mesmo perfil que você, mesmo nível de frustração em {segmento}. Há 8 meses era invisível no mercado. Hoje? Faturamento 10x maior, reconhecido como autoridade, palestrando em eventos, sendo DISPUTADO por clientes premium. A transformação foi tão rápida que ele mesmo não acreditou. E sabe qual foi o segredo? Ele parou de pensar pequeno. Parou de pedir migalhas e começou a exigir o banquete. Se você vai fazer o mesmo esforço, por que se contentar com resultados medianos? Por que não dominar completamente {segmento}? Por que não ser A referência? Por que não ter clientes fazendo FILA para trabalhar com você? Por que não cobrar 5x mais? Por que não ter um negócio que roda sem você? Esse é seu potencial REAL. Não para ser "mais um", mas para ser O cara.""",
                'casos_transformacao': [
                    'Cliente invisível que virou autoridade em 8 meses',
                    'Transformação de faturamento 10x com mesmo esforço'
                ],
                'visualizacao_futuro': 'Clientes fazendo fila, cobrando 5x mais, reconhecimento como autoridade',
                'ambicao_expandida': 'De sobrevivente para dominador total do segmento',
                'transicao': "Agora compare essa visão com sua realidade atual..."
            },
            'tensao_maxima': {
                'tempo': '3-4 minutos',
                'objetivo': 'AMPLIFICAR gap entre atual e ideal',
                'drivers_ativados': ['Identidade Aprisionada'],
                'script': f"""Olha o ABISMO entre onde você está e onde poderia estar. De um lado: você lutando, se esforçando, trabalhando dobrado para resultados medianos em {segmento}. Do outro: você dominando, clientes disputando sua atenção, cobrando premium, sendo reconhecido. Duas versões de VOCÊ. Uma frustrada, outra realizada. Uma sobrevivendo, outra prosperando. Uma trabalhando PARA o mercado, outra fazendo o mercado trabalhar para ela. E a diferença entre essas duas versões não é talento. Não é sorte. Não é "momento certo". É DECISÃO. É parar de se identificar como "alguém que luta" e começar a se ver como "alguém que domina". Você não é um lutador. Você é um DOMINADOR. Pare de aceitar migalhas.""",
                'gap_devastador': 'Contraste cruel entre versão atual e potencial',
                'identidade_conflito': 'Lutador vs Dominador - qual identidade escolher',
                'ponto_virada': 'Reconhecimento que a diferença é decisão, não circunstância',
                'transicao': "A pergunta não é SE você tem potencial..."
            },
            'necessidade_inevitavel': {
                'tempo': '4-5 minutos',
                'objetivo': 'Tornar mudança INEVITÁVEL e urgente',
                'drivers_ativados': ['Método vs Sorte', 'Decisão Binária'],
                'script': f"""A pergunta é COMO você vai ativar esse potencial. Porque você pode continuar tentando sozinho - cortando mato com foice, reinventando a roda, aprendendo na base da tentativa e erro. Ou pode pegar a AUTOESTRADA. O método que já funcionou para centenas de pessoas como você. O sistema que elimina 80% dos erros e acelera 300% os resultados. A diferença é tempo. Sozinho você chega lá? Talvez. Em 5 anos. Errando muito. Sofrendo muito. Ou você chega em 6 meses, com orientação, sem os furos, direto ao ponto. E agora você tem 30 segundos para decidir: vai continuar no modo "tentativa" ou vai entrar no modo "execução"? Porque não existe meio termo. Ou você DECIDE que vai dominar {segmento} nos próximos 6 meses, ou aceita que vai continuar na mediocridade. Não existe terceira opção.""",
                'metodo_vs_caos': 'Tentativa sozinho vs Sistema comprovado',
                'mentor_necessario': 'Orientação elimina 80% dos erros',
                'decisao_binaria': 'Dominação em 6 meses ou mediocridade permanente',
                'ponte_oferta': "E é exatamente isso que eu vou te mostrar agora...",
                'estado_mental_ideal': 'TENSÃO MÁXIMA, URGÊNCIA, NECESSIDADE DE SOLUÇÃO IMEDIATA'
            },
            'metricas_devastacao': {
                'indicadores_sucesso': [
                    'Silêncio absoluto durante ativação',
                    'Comentários emocionais no chat: "isso sou eu"',
                    'Perguntas sobre quando abre inscrições',
                    'Ansiedade visível para a oferta'
                ],
                'sinais_resistencia': [
                    'Questionamentos técnicos excessivos',
                    'Tentativa de mudança de assunto',
                    'Objeções imediatas de preço/tempo'
                ],
                'momento_ideal_pitch': 'Quando perguntam como sair da situação',
                'follow_up_pos': 'Manter urgência através de callbacks dos drivers ativados'
            }
        }
    
    def _create_format_variations(
        self, 
        complete_script: Dict[str, Any], 
        context_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Cria variações por formato"""
        
        return {
            'webinar': {
                'duracao_total': '15-20 minutos',
                'adaptacoes': [
                    'Usar chat para engajamento',
                    'Pausas para perguntas retóricas',
                    'Slides de apoio visual'
                ],
                'timing': 'Últimos 20 minutos antes da oferta'
            },
            'evento_presencial': {
                'duracao_total': '25-35 minutos',
                'adaptacoes': [
                    'Interação direta com audiência',
                    'Movimentação no palco',
                    'Provas visuais físicas'
                ],
                'timing': 'Distribuído ao longo do evento'
            },
            'cpl_3_aulas': {
                'duracao_total': '10-15 minutos',
                'adaptacoes': [
                    'Construção gradual ao longo das aulas',
                    'Callbacks entre aulas',
                    'Intensificação na aula 3'
                ],
                'timing': 'Final da aula 3'
            },
            'lives_aquecimento': {
                'duracao_total': '5-8 minutos por live',
                'adaptacoes': [
                    'Sementes em cada live',
                    'Preparação subliminar',
                    'Crescimento de intensidade'
                ],
                'timing': 'Distribuído nas lives'
            }
        }
    
    def _create_emotional_escalation(self, sequence: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Cria escalada emocional"""
        
        return {
            'curva_intensidade': [
                {'fase': seq['fase'], 'intensidade': seq['intensidade']} 
                for seq in sequence
            ],
            'pontos_pico': [
                seq['fase'] for seq in sequence 
                if seq['intensidade'] in ['Máxima', 'Definitiva']
            ],
            'momentos_alivio': [
                seq['fase'] for seq in sequence 
                if seq['intensidade'] == 'Esperançosa'
            ]
        }
    
    def _identify_critical_points(self, sequence: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Identifica pontos críticos"""
        
        critical_points = []
        
        for seq in sequence:
            if seq['intensidade'] in ['Máxima', 'Definitiva']:
                critical_points.append({
                    'fase': seq['fase'],
                    'momento': f"Durante {seq['objetivo'].lower()}",
                    'risco': 'Perda de audiência se muito intenso',
                    'oportunidade': 'Máximo impacto emocional',
                    'gestao': 'Monitorar reações e ajustar intensidade'
                })
        
        return critical_points
    
    def _create_phase_transitions(self, sequence: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Cria transições entre fases"""
        
        transitions = []
        
        for i in range(len(sequence) - 1):
            current_phase = sequence[i]['fase']
            next_phase = sequence[i + 1]['fase']
            
            transition_key = f"{current_phase}_para_{next_phase}"
            transition_text = self.transition_templates.get(
                transition_key, 
                f"Transição de {current_phase} para {next_phase}"
            )
            
            transitions.append({
                'de': current_phase,
                'para': next_phase,
                'script': transition_text,
                'tempo': '15-30 segundos',
                'tecnica': 'Ponte emocional suave'
            })
        
        return transitions
    
    def _create_success_metrics(self) -> Dict[str, Any]:
        """Cria métricas de sucesso"""
        
        return {
            'indicadores_durante': [
                'Silêncio absoluto durante ativação',
                'Comentários emocionais no chat',
                'Perguntas sobre quando abre inscrições',
                'Concordância física (acenar cabeça)'
            ],
            'indicadores_apos': [
                'Ansiedade visível para a oferta',
                'Perguntas sobre preço/formato',
                'Comentários "já quero comprar"',
                'Objeções minimizadas'
            ],
            'sinais_resistencia': [
                'Questionamentos técnicos excessivos',
                'Mudança de assunto',
                'Objeções imediatas',
                'Linguagem corporal fechada'
            ],
            'metricas_conversao': {
                'engajamento': 'Tempo de atenção por fase',
                'emocional': 'Reações emocionais geradas',
                'comportamental': 'Ações tomadas após ativação',
                'conversao': 'Taxa de conversão pós-pré-pitch'
            }
        }
    
    def _calculate_total_duration(self, orchestration: Dict[str, Any]) -> str:
        """Calcula duração total"""
        
        sequence = orchestration.get('sequencia_psicologica', [])
        
        total_min = 0
        total_max = 0
        
        for phase in sequence:
            duration = phase.get('duracao', '3-4 minutos')
            
            # Extrai números da duração
            import re
            numbers = re.findall(r'\d+', duration)
            if len(numbers) >= 2:
                total_min += int(numbers[0])
                total_max += int(numbers[1])
            elif len(numbers) == 1:
                total_min += int(numbers[0])
                total_max += int(numbers[0])
        
        return f"{total_min}-{total_max} minutos"
    
    def _calculate_max_intensity(self, orchestration: Dict[str, Any]) -> str:
        """Calcula intensidade máxima"""
        
        sequence = orchestration.get('sequencia_psicologica', [])
        
        intensities = [phase.get('intensidade', 'Baixa') for phase in sequence]
        
        if 'Máxima' in intensities:
            return 'Máxima'
        elif 'Alta' in intensities:
            return 'Alta'
        elif 'Crescente' in intensities:
            return 'Crescente'
        else:
            return 'Média'
    
    def _generate_fallback_pre_pitch_system(self, context_data: Dict[str, Any]) -> Dict[str, Any]:
        """Gera sistema de pré-pitch básico como fallback"""
        
        segmento = context_data.get('segmento', 'negócios')
        
        return {
            'orquestracao_emocional': {
                'sequencia_psicologica': [
                    {
                        'fase': 'quebra',
                        'objetivo': 'Quebrar padrão e despertar consciência',
                        'duracao': '3-5 minutos',
                        'intensidade': 'Alta',
                        'drivers_utilizados': ['Diagnóstico Brutal'],
                        'resultado_esperado': 'Desconforto produtivo'
                    },
                    {
                        'fase': 'vislumbre',
                        'objetivo': 'Mostrar possibilidades',
                        'duracao': '5-7 minutos',
                        'intensidade': 'Esperançosa',
                        'drivers_utilizados': ['Método vs Sorte'],
                        'resultado_esperado': 'Desejo de mudança'
                    },
                    {
                        'fase': 'necessidade',
                        'objetivo': 'Criar necessidade de solução',
                        'duracao': '3-4 minutos',
                        'intensidade': 'Definitiva',
                        'drivers_utilizados': ['Relógio Psicológico'],
                        'resultado_esperado': 'Urgência de ação'
                    }
                ]
            },
            'roteiro_completo': {
                'abertura': {
                    'tempo': '3-5 minutos',
                    'objetivo': 'Quebrar padrão e despertar consciência',
                    'script': f"Deixa eu te fazer uma pergunta sobre {segmento}... Há quanto tempo você está no mesmo nível? A verdade é que a maioria dos profissionais trabalha muito mas não sai do lugar.",
                    'frases_chave': [
                        f"A verdade sobre {segmento} que ninguém te conta",
                        "Isso vai doer, mas precisa ser dito"
                    ],
                    'transicao': "E sabe por que isso acontece?"
                },
                'desenvolvimento': {
                    'tempo': '8-12 minutos',
                    'objetivo': 'Amplificar dor e mostrar possibilidades',
                    'script': f"Cada dia que passa sem otimizar {segmento} é dinheiro saindo do seu bolso. Enquanto você está 'pensando', seus concorrentes estão agindo. Mas existe um caminho diferente...",
                    'momentos_criticos': [
                        "Cálculo da perda financeira por inação",
                        "Comparação com concorrentes que agem"
                    ],
                    'escalada_emocional': "Aumentar pressão gradualmente, depois mostrar esperança"
                },
                'fechamento': {
                    'tempo': '2-3 minutos',
                    'objetivo': 'Transição para solução',
                    'script': f"Agora você tem duas escolhas em {segmento}: continuar como está ou seguir um método comprovado. Eu vou te mostrar exatamente como sair dessa situação...",
                    'ponte_oferta': "Mas antes, preciso saber se você está realmente pronto para mudar...",
                    'estado_mental_ideal': "Ansioso pela solução, pronto para agir"
                }
            },
            'validation_status': 'FALLBACK_VALID',
            'generation_timestamp': time.time(),
            'fallback_mode': True,
            'duracao_total': '13-20 minutos'
        }

# Instância global
pre_pitch_architect = PrePitchArchitect()