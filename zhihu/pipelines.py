# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ZhihuPipeline(object):
        
    def process_item(self, item, spider):
        with open('output/Topic.txt', 'w+') as file:
            title = item['title']
            question = item['question']
            file.write("title:" + str(title) + '\n\n')
            for i, tag in enumerate(question):
                file.write("Topic" + str(i+1) + ":" + str(tag.get_text()).strip('\n') + '\n')
        return item
