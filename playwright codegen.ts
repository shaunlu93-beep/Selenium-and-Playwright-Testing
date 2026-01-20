import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSeKA5va7ez55lqpC8kMgy01V3F8tkqoATrDhTIfsTe8KH6jkQ%2Fviewform%3Fusp%3Dsend_form&dsh=S1882746108%3A1766443000923601&followup=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSeKA5va7ez55lqpC8kMgy01V3F8tkqoATrDhTIfsTe8KH6jkQ%2Fviewform%3Fusp%3Dsend_form&ifkv=Ac2yZaUveYy5LW_Mgnx2D-E5xsZjgzmCCLtFwO4zhu--aHityFC28u6-BPinqKFvVoXLT-9RPMdHWw&ltmpl=forms&osid=1&passive=1209600&service=wise&flowName=GlifWebSignIn&flowEntry=ServiceLogin');
  await page.getByRole('textbox', { name: '電子郵件地址或電話號碼' }).click();
  await page.getByRole('textbox', { name: '電子郵件地址或電話號碼' }).fill('pajh113031@pajh.hcc.edu.tw');
  await page.getByRole('textbox', { name: '電子郵件地址或電話號碼' }).press('Enter');
  await page.getByRole('textbox', { name: '輸入您的密碼' }).click();
  await page.getByRole('textbox', { name: '輸入您的密碼' }).fill('F133156219');
  await page.getByRole('button', { name: '下一步' }).click();
  await page.getByRole('textbox', { name: '座號： 將這個問題設為必填' }).click();
  await page.getByRole('textbox', { name: '座號： 將這個問題設為必填' }).fill('Hello');
  await page.getByRole('textbox', { name: '姓名： 將這個問題設為必填' }).click();
  await page.getByRole('textbox', { name: '姓名： 將這個問題設為必填' }).fill('World!');
  await page.getByRole('radio', { name: '是' }).click();
  await page.getByRole('textbox', { name: '最想去的城市： 將這個問題設為必填' }).click();
  await page.getByRole('textbox', { name: '最想去的城市： 將這個問題設為必填' }).fill('123');
  await page.getByRole('button', { name: 'Submit' }).click();
  await expect(page.getByText('家族旅遊問卷調查我們已經收到您回覆的表單。提交其他回應')).toBeVisible();
});