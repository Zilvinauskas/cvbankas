from patchright.sync_api import Browser, Page, sync_playwright

pr = sync_playwright().start()
print(type(pr))