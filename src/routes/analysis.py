#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Rotas de Análise
Sistema completo de análise de mercado com agentes especializados
"""

import logging
from flask import Blueprint, render_template, request, jsonify
from services.ultra_detailed_analysis_engine import ultra_analysis_engine
from services.enhanced_ui_manager import enhanced_ui_manager
from services.context_intelligence_engine import context_intelligence_engine
from services.professional_report_manager import professional_report_manager
import traceback
import uuid
import time
from datetime import datetime

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Blueprint para análises
analysis_bp = Blueprint('analysis', __name__)

@analysis_bp.route('/')
def index():
    """Página principal com interface aprimorada"""
    try:
        return render_template('enhanced_interface.html')
    except Exception as e:
        logger.error(f"Erro ao carregar interface: {e}")
        return render_template('enhanced_interface.html')

@analysis_bp.route('/api/analyze', methods=['POST'])
def start_analysis():
    """Inicia análise ultra-detalhada"""
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                'success': False,
                'message': 'Dados não fornecidos'
            }), 400

        # Validações essenciais
        if not data.get('segmento'):
            return jsonify({
                'success': False,
                'message': 'Segmento de mercado é obrigatório'
            }), 400

        # Gera ID da sessão
        session_id = f"session_{int(time.time() * 1000)}_{uuid.uuid4().hex[:12]}"

        logger.info(f"🎯 Iniciando análise para sessão: {session_id}")
        logger.info(f"📊 Segmento: {data.get('segmento')}")
        logger.info(f"🎁 Produto: {data.get('produto', 'N/A')}")

        # Executa análise real usando o engine disponível
        try:
            from services.ultra_detailed_analysis_engine import ultra_analysis_engine
            
            # Executa análise completa
            resultado_analise = ultra_analysis_engine.generate_gigantic_analysis(
                data, session_id
            )

            # Salva no banco automaticamente
            from database import db_manager
            try:
                db_record = db_manager.create_analysis({
                    **data,
                    **resultado_analise,
                    'analysis_type': 'ultra_detailed',
                    'session_id': session_id,
                    'status': 'completed'
                })
                if db_record:
                    resultado_analise['database_id'] = db_record.get('id')
                    logger.info(f"✅ Análise salva no banco: ID {db_record.get('id')}")
            except Exception as db_error:
                logger.warning(f"⚠️ Erro ao salvar no banco: {db_error}")

            return jsonify({
                'success': True,
                'message': 'Análise concluída com sucesso',
                'session_id': session_id,
                'data': resultado_analise
            })

        except Exception as analysis_error:
            logger.error(f"❌ Erro ao executar análise: {analysis_error}")
            return jsonify({
                'success': False,
                'message': f'Erro na análise: {str(analysis_error)}'
            }), 500

    except Exception as e:
        logger.error(f"❌ Erro geral na rota de análise: {e}")
        logger.error(traceback.format_exc())

        return jsonify({
            'success': False,
            'error': 'internal_server_error',
            'message': 'Erro interno do servidor',
            'details': str(e) if logger.level <= logging.DEBUG else None
        }), 500

@analysis_bp.route('/api/progress/<session_id>')
def get_progress(session_id):
    """Obtém progresso da análise"""
    try:
        # Busca progresso nos relatórios salvos
        from services.auto_save_manager import auto_save_manager
        etapas_salvas = auto_save_manager.listar_etapas_salvas(session_id)

        if not etapas_salvas:
            progress = None
        else:
            # Reconstrói dados a partir das etapas salvas
            analysis_data = {}
            for etapa_nome in etapas_salvas.keys():
                dados_etapa = auto_save_manager.recuperar_etapa(etapa_nome, session_id)
                if dados_etapa and dados_etapa.get('status') == 'sucesso':
                    analysis_data[etapa_nome] = dados_etapa.get('dados')

            progress = {
                'status': 'completed' if analysis_data else 'in_progress',
                'data': analysis_data,
                'session_id': session_id
            }

        if not progress:
            return jsonify({
                'status': 'not_found',
                'progress': 0,
                'message': 'Sessão não encontrada'
            }), 404

        return jsonify(progress)

    except Exception as e:
        logger.error(f"❌ Erro ao obter progresso: {e}")
        return jsonify({
            'status': 'error',
            'progress': 0,
            'message': 'Erro ao obter progresso'
        }), 500

@analysis_bp.route('/api/save_analysis', methods=['POST'])
def save_analysis():
    """Salva análise no banco de dados"""
    try:
        data = request.get_json()
        session_id = data.get('session_id')

        if not session_id:
            return jsonify({
                'success': False,
                'message': 'ID da sessão não fornecido'
            }), 400

        # Obtém dados da análise
        try:
            # Tenta executar análise se não existe
            from services.auto_save_manager import auto_save_manager
            etapas_salvas = auto_save_manager.listar_etapas_salvas(session_id)

            if not etapas_salvas:
                # Executa análise se não foi executada ainda
                dados_entrada = {
                    'segmento': 'análise solicitada',
                    'session_id': session_id
                }
                resultado_analise = ultra_analysis_engine.generate_gigantic_analysis(dados_entrada, session_id)

        except Exception as e:
            logger.warning(f"Não foi possível executar análise: {e}")

        # Busca progresso nos relatórios salvos
        from services.auto_save_manager import auto_save_manager
        etapas_salvas = auto_save_manager.listar_etapas_salvas(session_id)

        analysis_data = {}
        if etapas_salvas:
            for etapa_nome in etapas_salvas.keys():
                dados_etapa = auto_save_manager.recuperar_etapa(etapa_nome, session_id)
                if dados_etapa and dados_etapa.get('status') == 'sucesso':
                    analysis_data[etapa_nome] = dados_etapa.get('dados')

        progress = {
            'status': 'completed' if analysis_data else 'in_progress',
            'data': analysis_data,
            'session_id': session_id
        }

        if not progress or progress.get('status') != 'completed':
            return jsonify({
                'success': False,
                'message': 'Análise não está completa'
            }), 400

        # Salva no banco (implementar conforme necessário)
        success = professional_report_manager.save_analysis_to_database(
            session_id, 
            progress.get('data', {})
        )

        if success:
            return jsonify({
                'success': True,
                'message': 'Análise salva com sucesso'
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Erro ao salvar análise'
            }), 500

    except Exception as e:
        logger.error(f"❌ Erro ao salvar análise: {e}")
        return jsonify({
            'success': False,
            'message': 'Erro interno do servidor'
        }), 500

@analysis_bp.route('/archaeological')
def archaeological_interface():
    """Interface arqueológica especializada"""
    try:
        return render_template('archaeological_interface.html')
    except Exception as e:
        logger.error(f"Erro ao carregar interface arqueológica: {e}")
        return render_template('enhanced_interface.html')

@analysis_bp.route('/forensic')  
def forensic_interface():
    """Interface forense especializada"""
    try:
        return render_template('forensic_interface.html')
    except Exception as e:
        logger.error(f"Erro ao carregar interface forense: {e}")
        return render_template('enhanced_interface.html')

@analysis_bp.route('/api/render_analysis/<session_id>')
def render_analysis_results(session_id):
    """Renderiza resultados da análise com UI aprimorada"""
    try:
        # Busca progresso nos relatórios salvos
        from services.auto_save_manager import auto_save_manager
        etapas_salvas = auto_save_manager.listar_etapas_salvas(session_id)

        analysis_data = {}
        if etapas_salvas:
            for etapa_nome in etapas_salvas.keys():
                dados_etapa = auto_save_manager.recuperar_etapa(etapa_nome, session_id)
                if dados_etapa and dados_etapa.get('status') == 'sucesso':
                    analysis_data[etapa_nome] = dados_etapa.get('dados')

        progress = {
            'status': 'completed' if analysis_data else 'in_progress',
            'data': analysis_data,
            'session_id': session_id
        }


        if not progress or progress.get('status') != 'completed':
            return jsonify({
                'success': False,
                'message': 'Análise não encontrada ou incompleta'
            }), 404

        analysis_data = progress.get('data', {})

        # Renderiza componentes com UI manager
        rendered_components = {}

        # Avatar visceral
        if 'avatar_visceral_ultra' in analysis_data:
            rendered_components['avatar'] = enhanced_ui_manager.render_visceral_avatar(
                analysis_data
            )

        # Drivers mentais
        if 'drivers_mentais_customizados' in analysis_data:
            rendered_components['drivers'] = enhanced_ui_manager.render_drivers_arsenal(
                analysis_data.get('drivers_mentais_customizados', {})
            )

        # Provas visuais
        if 'provas_visuais_sugeridas' in analysis_data:
            rendered_components['provas'] = enhanced_ui_manager.render_provis_arsenal(
                analysis_data.get('provas_visuais_sugeridas', {})
            )

        # Métricas forenses
        if 'metricas_forenses' in analysis_data:
            rendered_components['metricas'] = enhanced_ui_manager.render_forensic_metrics(
                analysis_data.get('metricas_forenses', {})
            )

        return jsonify({
            'success': True,
            'components': rendered_components,
            'metadata': {
                'session_id': session_id,
                'timestamp': analysis_data.get('timestamp'),
                'segmento': analysis_data.get('segmento'),
                'produto': analysis_data.get('produto')
            }
        })

    except Exception as e:
        logger.error(f"❌ Erro ao renderizar análise: {e}")
        return jsonify({
            'success': False,
            'message': 'Erro ao renderizar resultados'
        }), 500

# Handlers de erro
@analysis_bp.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'message': 'Endpoint não encontrado'
    }), 404

@analysis_bp.errorhandler(500)
def internal_error(error):
    logger.error(f"❌ Erro interno do servidor: {error}")
    return jsonify({
        'success': False,
        'message': 'Erro interno do servidor'
    }), 500

# Registro das rotas
logger.info("✅ Rotas de análise registradas com sucesso")