from opentelemetry.metrics import get_meter #Falando para o OTel que esse será o professor que irei usar

from opentelemetry.sdk.resources import Resource, SERVICE_NAME, SERVICE_VERSION
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader, ConsoleMetricExporter

from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter


#Resource - Explic para o OTel o que é o nosso serviço
#O service_name resgat o nome do servio
resource = Resource(
    attributes={SERVICE_NAME: 'meu-app',
                 SERVICE_VERSION: '0.1'}

)

#Reader - Leitor periódico das métricas
#Exportando as métricas para o console
reader_console = PeriodicExportingMetricReader(ConsoleMetricExporter())

#OTLP - Protocolo padronizado para a transmissão de dados de telemetria no OTel
#Exporter - Trnsmite sem perda de informação
#Para subir no localhost, basta deixar vazio o ()
reader_otlp = PeriodicExportingMetricReader(OTLPMetricExporter())

#Provedor de métricas, de onde criaremos as métricas
provider = MeterProvider(
    resource=resource, metric_readers=[reader_console,reader_otlp]
)

#A partir do nosso provider, conseguimos criar métricas
meter = get_meter('meter', meter_provider=provider)

#Criação do contador
conter = meter.create_counter(
    name='carros.passando',
    unit='1',
    description='Carros passando na minha rua'
)

conter.add(amount=1, attributes={
    'modelo': 'Monza',
    'cor': 'Preto'
    }
)

conter.add(amount=1, attributes={
    'modelo': 'Fusca',
    'cor': 'Preto'
    }
)

conter.add(amount=6, attributes={
    'modelo': 'Marea',
    'cor': 'Prata'
    }
)