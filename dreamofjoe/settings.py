BOT_NAME = 'dreamofjoe'
SPIDER_MODULES = ['dreamofjoe.spiders']
NEWSPIDER_MODULE = 'dreamofjoe.spiders'
ROBOTSTXT_OBEY = True
LOG_LEVEL = 'WARNING'
ITEM_PIPELINES = {
   'dreamofjoe.pipelines.DreamofjoePipeline': 300,
}
