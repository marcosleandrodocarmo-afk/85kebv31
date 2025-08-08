#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Aplicação Principal
Servidor Flask para análise de mercado ultra-detalhada
"""

import os
import sys
import time
import logging
from typing import Dict, List, Any, Optional
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from datetime import datetime

# Adiciona src ao path se necessário
if 'src' not in sys.path:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Configuração de logging
os.makedirs('logs', exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('logs/arqv30.log', encoding='utf-8')
    ]
)

logger = logging.getLogger(__name__)

def create_app():
    """Cria e configura a aplicação Flask"""

    # Carrega variáveis de ambiente
    from services.environment_loader import environment_loader

    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

    # Configuração CORS
    CORS(app, origins=os.getenv('CORS_ORIGINS', '*').split(','))

    # Importa blueprints essenciais primeiro
    try:
        from routes.analysis import analysis_bp
        logger.info("✅ Rota de análise carregada com sucesso")
    except Exception as e:
        logger.error(f"❌ ERRO CRÍTICO ao carregar rota de análise: {e}")
        logger.error("🔧 Verifique o arquivo routes/analysis.py e services/ultra_detailed_analysis_engine.py")
        raise e  # Para a aplicação se não conseguir carregar rota essencial

    # Importa outras rotas com fallback
    enhanced_analysis_bp = None
    progress_bp = None
    user_bp = None
    files_bp = None
    pdf_bp = None
    monitoring_bp = None
    forensic_bp = None
    mcp_bp = None

    try:
        from routes.enhanced_analysis import enhanced_analysis_bp
        logger.info("✅ Rota de análise aprimorada carregada")
    except Exception as e:
        logger.warning(f"⚠️ Erro ao importar enhanced_analysis: {e}")

    try:
        from routes.progress import progress_bp
        from routes.user import user_bp
        from routes.files import files_bp
        from routes.pdf_generator import pdf_bp
        from routes.monitoring import monitoring_bp
        from routes.forensic_analysis import forensic_bp
        from routes.mcp import mcp_bp
        logger.info("✅ Todas as rotas auxiliares importadas")
    except ImportError as e:
        logger.warning(f"⚠️ Algumas rotas auxiliares falharam: {e}")

    # Registra blueprints com tratamento de erros
    blueprints_to_register = [
        (analysis_bp, '', 'analysis'),  # Sem prefixo para /api/analyze funcionar
        (enhanced_analysis_bp, '/api', 'enhanced_analysis'),
        (progress_bp, '/api', 'progress'),
        (user_bp, '/api', 'user'),
        (files_bp, '/api', 'files'),
        (pdf_bp, '/api', 'pdf'),
        (monitoring_bp, '/api', 'monitoring'),
        (forensic_bp, '/api/forensic', 'forensic'),
        (mcp_bp, '/api', 'mcp')
    ]

    for blueprint, prefix, name in blueprints_to_register:
        try:
            if blueprint:
                app.register_blueprint(blueprint, url_prefix=prefix)
                logger.info(f"✅ Blueprint {name} registrado")
        except Exception as e:
            logger.warning(f"⚠️ Erro ao registrar blueprint {name}: {e}")
            continue

    @app.route('/')
    def index():
        """Página principal"""
        return render_template('enhanced_index.html')

    @app.route('/archaeological')
    def archaeological():
        """Interface arqueológica"""
        return render_template('enhanced_interface.html')

    @app.route('/forensic')
    def forensic():
        """Interface forense"""
        return render_template('forensic_interface.html')

    @app.route('/unified')
    def unified():
        """Interface unificada"""
        return render_template('unified_interface.html')

    @app.route('/api/app_status')
    def app_status():
        """Status da aplicação"""
        try:
            from services.ai_manager import ai_manager
            from services.production_search_manager import production_search_manager
            from database import db_manager

            ai_status = ai_manager.get_provider_status()
            search_status = production_search_manager.get_provider_status()
            db_status = db_manager.test_connection()

            return jsonify({
                'status': 'healthy',
                'timestamp': datetime.now().isoformat(),
                'version': '2.0.0',
                'services': {
                    'ai_providers': {
                        'available': len([p for p in ai_status.values() if p['available']]),
                        'total': len(ai_status),
                        'providers': ai_status
                    },
                    'search_providers': {
                        'available': len([p for p in search_status.values() if p['available']]),
                        'total': len(search_status),
                        'providers': search_status
                    },
                    'database': {
                        'connected': db_status
                    }
                }
            })
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': str(e),
                'timestamp': datetime.now().isoformat()
            }), 500

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Endpoint não encontrado'}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Erro interno do servidor'}), 500

    return app

def main():
    """Função principal"""

    print("🚀 ARQV30 Enhanced v2.0 - Iniciando aplicação...")

    try:
        # Cria aplicação
        app = create_app()

        # Configurações do servidor
        host = os.getenv('HOST', '0.0.0.0')
        port = int(os.getenv('PORT', 5000))
        debug = os.getenv('FLASK_ENV', 'production') == 'development'

        # Tenta diferentes portas se a principal estiver ocupada
        max_attempts = 5
        for attempt in range(max_attempts):
            try:
                import socket
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.bind((host, port))
                sock.close()
                break
            except OSError:
                logger.warning(f"⚠️ Porta {port} ocupada, tentando {port + 1}")
                port += 1
        else:
            logger.error(f"❌ Não foi possível encontrar porta disponível após {max_attempts} tentativas")
            port = 5000  # Use a porta padrão mesmo assim

        print(f"🌐 Servidor: http://{host}:{port}")
        print(f"🔧 Modo: {'Desenvolvimento' if debug else 'Produção'}")
        print(f"📊 Interface: Análise Ultra-Detalhada de Mercado")
        print(f"🤖 IA: Gemini 2.5 Pro + Groq + Fallbacks")
        print(f"🔍 Pesquisa: WebSailor + Google + Múltiplos Engines")
        print(f"💾 Banco: Supabase + Arquivos Locais")
        print(f"🛡️ Sistema: Ultra-Robusto com Salvamento Automático")

        print("\n" + "=" * 60)
        print("✅ ARQV30 Enhanced v2.0 PRONTO!")
        print("=" * 60)
        print("Pressione Ctrl+C para parar o servidor")
        print("=" * 60)

        # Inicia servidor
        app.run(
            host=host,
            port=port,
            debug=debug,
            threaded=True
        )

    except KeyboardInterrupt:
        print("\n\n✅ Servidor encerrado pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro ao iniciar servidor: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()